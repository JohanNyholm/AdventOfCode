from collections import defaultdict
import re

import common


def parse_input(file_name):
    settings = []
    for line in common.get_input(file_name):
        index1, index2, char, password = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups(0)
        indexes = [int(v) - 1 for v in (index1, index2)]
        settings.append({
            'indexes': indexes,
            'char': char,
            'password': password,
        })
    return settings


def char_lookup(password) -> defaultdict(set):
    lookup = defaultdict(set)
    for i, c in enumerate(password):
        lookup[c].add(i)
    return lookup


def solve(rows):
    num_correct = 0
    for row in rows:
        char_indexes = char_lookup(row['password'])[row['char']]
        num_char_matches = 0
        for i in row['indexes']:
            if i in char_indexes:
                num_char_matches += 1
        if num_char_matches == 1:
            num_correct += 1
    return num_correct


file_name = '2.txt'
rows = parse_input(file_name)
solution = solve(rows)
print(solution)
