import re

import common


def parse_input(file_name):
    return [
        {
            kv[0]: kv[1]
            for kv
            in re.findall(r'(?:(\S+)\:(\S+))', passport_raw)
        } for passport_raw in common.get_input(file_name).split('\n\n')
    ]


def _validate_passport(passport, required_fields):
    return not required_fields.difference(set(passport.keys()))


def solve(passports, required_fields):
    return sum(
        _validate_passport(
            passport,
            required_fields
        ) for passport in passports
    )


required_fields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
])
file_name = '04.txt'
passports = parse_input(file_name)
solution = solve(passports, required_fields)
print(solution)
