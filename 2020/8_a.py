import re
from functools import lru_cache

import common


def _parse_instruction(instruction_string):
    command, arg = re.search(
        r'^([\w]+) ([\+\-]\d+)$',
        instruction_string
    ).groups()
    return {
        'command': command,
        'arg': int(arg),
    }


def parse_input(file_name):
    return [
        _parse_instruction(instruction_string)
        for instruction_string in common.get_input_lines(file_name)
    ]


def acc(program_state, arg):
    program_state['accumulator'] += arg
    program_state['program_counter'] += 1


def jmp(program_state, arg):
    program_state['program_counter'] += arg


def nop(program_state, arg):
    program_state['program_counter'] += 1


COMMANDS = {
    'acc': acc,
    'jmp': jmp,
    'nop': nop,
}
def execute(instructions):
    program_counter_history = set([])
    program_state = {
        'program_counter': 0,
        'accumulator': 0,
    }
    while (program_state['program_counter'] not in program_counter_history):
        program_counter_history.add(program_state['program_counter'])
        instruction = instructions[program_state['program_counter']]
        COMMANDS[instruction['command']](program_state, instruction['arg'])
    return {
        'accumulator': program_state['accumulator'],
    }

def solve(instructions):
    return execute(instructions)['accumulator']


file_name = '8.txt'
instructions = parse_input(file_name)
solution = solve(instructions)
print(solution)
