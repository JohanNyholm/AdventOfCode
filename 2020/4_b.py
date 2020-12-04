import re
from functools import partial

import common


def parse_input(file_name):
    passports_raw = []
    passport_raw = ''
    for line in common.get_input_lines(file_name):
        if not line:
            passports_raw.append(passport_raw)
            passport_raw = ''
            continue
        if passport_raw:
            passport_raw += ' ' + line
        else:
            passport_raw = line
    passports_raw.append(passport_raw)

    passports = []
    for passport_raw in passports_raw:
        passport = {}
        for kw_pair in passport_raw.split(' '):
            key, value = kw_pair.split(':')
            passport[key] = value
        passports.append(passport)

    return passports


def _parse_int(val, default=None):
    try:
        return int(val)
    except ValueError:
        return default


def _validate_int(value, min, max):
    return min <= _parse_int(value, 0) <= max


def _validate_hgt(value):
    match = re.search(r'^(\d+)in$', value)
    if match is not None:
        return _validate_int(match.group(1), 59, 76)
    match = re.search(r'^(\d+)cm$', value)
    if match is not None:
        return _validate_int(match.group(1), 150, 193)
    return False


def _validate_ecl(value):
    return value in set(['amb','blu', 'brn','gry', 'grn','hzl','oth'])


def _validate_regex(value, regex):
    return re.match(regex, value) is not None


def solve(passports, required_fields, validators):
    num_valid = 0
    for passport in passports:
        passport_keys = set(passport.keys())
        if required_fields.difference(passport_keys):
            continue
        if not all(validators[key](value) for key, value in passport.items() if key in validators):
            continue
        num_valid += 1
    return num_valid


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
validators = {
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
solution = solve(passports, required_fields, validators)
print(solution)
