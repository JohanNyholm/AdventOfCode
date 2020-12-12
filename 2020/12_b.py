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
    if any(amount % 90 != 0 for action_type, amount in actions if action_type in set(['L', 'R'])):
        raise('Only 90 degree angles supported')

    # translate west motions into negative east motions
    actions = _translate_actions(actions, {
        'W': {
            'action_type': 'E',
            'amount_transform': lambda v: -v
        }})
    # translate west motions into negative east motions
    actions = _translate_actions(actions, {
        'N': {
            'action_type': 'S',
            'amount_transform': lambda v: -v
        }})
    # translate left turns into negative right turns
    actions = _translate_actions(actions, {
        'L': {
            'action_type': 'R',
            'amount_transform': lambda v: -v
        }})
    # translate right turns to number of 90 degree turns
    actions = _translate_actions(actions, {
        'R': {
            'action_type': 'R',
            'amount_transform': lambda v: (v // 90) % 4
        }})
    waypoint = {'E': 10, 'S': -1}
    position = {'E': 0, 'S': 0}
    for action, amount in actions:
        if action == 'F':
            position['E'] += waypoint['E'] * amount
            position['S'] += waypoint['S'] * amount
        elif action == 'R':
            for _ in range(amount):
                waypoint['E'], waypoint['S'] = -waypoint['S'],  waypoint['E']
        elif action == 'E':
            waypoint['E'] += amount
        elif action == 'S':
            waypoint['S'] += amount
    return abs(position['E']) + abs(position['S'])


file_name = '12.txt'
actions = parse_input(file_name)
solution = solve(actions)
print(solution)
