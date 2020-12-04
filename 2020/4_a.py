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


def solve(passports, required_fields):
    num_valid = 0
    for passport in passports:
        passport_keys = set(passport.keys())
        if not required_fields.difference(passport_keys):
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
file_name = '4.txt'
passports = parse_input(file_name)
solution = solve(passports, required_fields)
print(solution)
