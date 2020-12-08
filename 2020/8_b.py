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
    exit_position = len(instructions)
    while (
        program_state['program_counter'] not in program_counter_history
        and program_state['program_counter'] != exit_position
    ):
        program_counter_history.add(program_state['program_counter'])
        instruction = instructions[program_state['program_counter']]
        COMMANDS[instruction['command']](program_state, instruction['arg'])
    return {
        'accumulator': program_state['accumulator'],
        'exit_code': 0 if program_state['program_counter'] == exit_position else 1
    }

def solve(instructions):
    program_counter_history = set([])
    program_state = {
        'program_counter': 0,
        'accumulator': 0,
    }
    num_instructions = len(instructions)
    exit_position = num_instructions

    flip_commands = ('jmp', 'nop') 
    for i in range(0, num_instructions):
        suspect_command = instructions[i]['command']
        if suspect_command not in flip_commands:
            continue
        instructions[i]['command'] = flip_commands[(flip_commands.index(suspect_command) + 1) % 2]
        exit_state = execute(instructions)
        instructions[i]['command'] = suspect_command
        if exit_state['exit_code'] == 0:
            return exit_state['accumulator']


file_name = '8.txt'
instructions = parse_input(file_name)
solution = solve(instructions)
print(solution)
