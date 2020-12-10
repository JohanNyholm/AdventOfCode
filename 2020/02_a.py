import re

import common


def parse_input(file_name):
    settings = []
    for line in common.get_input_lines(file_name):
        span_start, span_end, char, password = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups(0)
        span = [int(s) for s in (span_start, span_end)]
        settings.append({
            'span': span,
            'char': char,
            'password': password,
        })
    return settings


def solve(rows):
    num_correct = 0
    for row in rows:
        count = row['password'].count(row['char'])
        if row['span'][0] <= count <= row['span'][1]:
            num_correct += 1
    return num_correct


file_name = '02.txt'
rows = parse_input(file_name)
solution = solve(rows)
print(solution)
