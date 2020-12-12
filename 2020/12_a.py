import re

import common


def _parse_line(line):
    action_type, amount = re.search(r'^(\w)(\d+)$', line).groups()
    return action_type, int(amount)


def parse_input(file_name):
    return [
        _parse_line(line)
        for line in common.get_input_lines(file_name)
    ]


def _translate_actions(actions, transformations={}):
    def _translate(action_type, amount):
        if action_type in transformations:
            transformation = transformations[action_type]
            action_type = transformation['action_type']
            amount = transformation['amount_transform'](amount)
        return action_type, amount

    return [
        _translate(action_type, amount) for action_type, amount in actions
    ]


def solve(actions):
    turn_actions = set(['L', 'R'])
    if any(amount % 90 != 0 for action_type, amount in actions if action_type in turn_actions):
        raise('Only 90 degree angles supported')

    cardinal_directions = set(['E', 'W', 'N', 'S'])
    cardinal_actions = [(action_type, amount) for action_type, amount in actions if action_type in cardinal_directions]
    # translate west motions into negative east motions
    cardinal_actions = _translate_actions(cardinal_actions, {
        'W': {
            'action_type': 'E',
            'amount_transform': lambda v: -v
        }})
    # translate west motions into negative east motions
    cardinal_actions = _translate_actions(cardinal_actions, {
        'N': {
            'action_type': 'S',
            'amount_transform': lambda v: -v
        }})
    position = {
        'E': sum(amount for action_type, amount in cardinal_actions if action_type == 'E'),
        'S': sum(amount for action_type, amount in cardinal_actions if action_type == 'S'),
    }

    non_cardinal_actions = [(action, amount) for action, amount in actions if action not in cardinal_directions]
    # translate left turns into negative right turns
    non_cardinal_actions = _translate_actions(non_cardinal_actions, {
        'L': {
            'action_type': 'R',
            'amount_transform': lambda v: -v
        }})
    # translate right turns into number of 90 degree turns
    non_cardinal_actions = _translate_actions(non_cardinal_actions, {
        'R': {
            'action_type': 'R',
            'amount_transform': lambda v: (v // 90) % 4
        }})
    # Directions
    #      (N=3)
    # (W=2)     (E=0)
    #      (S=1)
    direction = 0
    direction_motions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for action_type, amount in non_cardinal_actions:
        if action_type == 'R':
            direction = (direction + amount) % 4
        elif action_type == 'F':
            motion = direction_motions[direction]
            position['E'] += motion[0] * amount
            position['S'] += motion[1] * amount

    return abs(position['E']) + abs(position['S'])


file_name = '12.txt'
actions = parse_input(file_name)
solution = solve(actions)
print(solution)
