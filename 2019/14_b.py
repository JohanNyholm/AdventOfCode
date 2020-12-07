import re
from collections import defaultdict

import common

def _parse_reaction(reaction_string):
    inputs_string, output_amount, output_chemical = re.search(
        r'^(.*) => (\d+) (\w+)$',
        reaction_string
    ).groups()
    inputs = {
        input_chemical: int(amount)
        for amount, input_chemical
        in re.findall(r'(\d+) ([\w ]+)', inputs_string)
    }
    return output_chemical, int(output_amount), inputs


def parse_input(file_name):
    return {
        output_chemical: {
            'output_amount': output_amount,
            'inputs': inputs,
        } for output_chemical, output_amount, inputs
        in (
            _parse_reaction(reaction_string)
            for reaction_string in common.get_input_lines(file_name)
        )
    }

FUEL = 'FUEL'
ORE = 'ORE'

def get_one_fuel(reactions, unused_chemicals, requirements):
    # print('req   : ', requirements.items())
    # print('unused: ', unused_chemicals.items())
    while(requirements.keys() != { ORE }):
        chemical, amount = requirements.popitem()
        if chemical == ORE:
            ore_amount = amount
            chemical, amount = requirements.popitem()
            requirements[ORE] = ore_amount

        reaction = reactions[chemical]
        reaction_output_amount = reaction['output_amount']
        num_reactions_required = abs(-amount // reaction_output_amount)
        for input_chemical, input_amount in reaction['inputs'].items():
            amount_required = num_reactions_required * input_amount - unused_chemicals[input_chemical]
            if amount_required > 0:
                requirements[input_chemical] += amount_required
                unused_chemicals[input_chemical] = 0
            else:
                unused_chemicals[input_chemical] = -amount_required

        unused_chemicals[chemical] += (num_reactions_required * reaction_output_amount - amount)
        # print('req   : ', requirements.items())
        # print('unused: ', unused_chemicals.items())

def solve(reactions):

    unused_chemicals = defaultdict(int)
    requirements = defaultdict(int)
    # print('req   : ', requirements.items())
    # print('unused: ', unused_chemicals.items())
    num_fuel = 0
    available_ore = 1000000000000
    while requirements[ORE] <= available_ore:
        for chemical, amount in reactions[FUEL]['inputs'].items():
            if unused_chemicals[chemical] >= amount:
                unused_chemicals[chemical] -= amount
            else:
                requirements[chemical] += (amount - unused_chemicals[chemical])
                unused_chemicals[chemical] = 0
        get_one_fuel(reactions, unused_chemicals, requirements)
        if requirements[ORE] <= available_ore:
            num_fuel += 1

    return num_fuel


file_name = '14_example_2.txt'
reactions = parse_input(file_name)

solution = solve(reactions)
print(solution)
