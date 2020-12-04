import re
from functools import partial

import common


def parse_input(file_name):
    return [
        {
            kv[0]: kv[1]
            for kv
            in re.findall(r'(?:(\S+)\:(\S+))', passport_raw)
        } for passport_raw in common.get_input(file_name).split('\n\n')
    ]


def _validate_int(value, min, max):
    return min <= int(value) <= max


def _validate_inches(value, min, max):
    match = re.search(r'^(\d+)in$', value)
    return match is not None and _validate_int(match.group(1), min, max)


def _validate_centimeters(value, min, max):
    match = re.search(r'^(\d+)cm$', value)
    return match is not None and _validate_int(match.group(1), min, max)


def _validate_hgt(value):
    return (
        _validate_inches(value, 59, 76)
        or _validate_centimeters(value, 150, 193)
    )


def _validate_ecl(value):
    return value in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])


def _validate_regex(value, regex):
    return re.match(regex, value) is not None


def _validate_passport(passport, required_fields, field_validators):
    return (
        not required_fields.difference(set(passport.keys()))
        and all(
            field_validators[key](value)
            for key, value in passport.items() if key in field_validators
        )
    )


def solve(passports, required_fields, field_validators):
    return sum(
        _validate_passport(
            passport,
            required_fields,
            field_validators
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
field_validators = {
    'byr': partial(_validate_int, min=1920, max=2002),
    'iyr': partial(_validate_int, min=2010, max=2020),
    'eyr': partial(_validate_int, min=2020, max=2030),
    'hgt': _validate_hgt,
    'hcl': partial(_validate_regex, regex=r'^#([\da-f]{6})$'),
    'ecl': _validate_ecl,
    'pid': partial(_validate_regex, regex=r'^([\d]{9})$'),
    # 'cid',
}
file_name = '4.txt'
passports = parse_input(file_name)
solution = solve(passports, required_fields, field_validators)
print(solution)
