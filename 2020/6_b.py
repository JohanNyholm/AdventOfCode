import common


CHAR_RANGE = [chr(v) for v in range(ord('a'), ord('z') + 1)]


def parse_input(file_name):
    return [
        [set(passenger) for passenger in group.split('\n')]
        for group in common.get_input(file_name).split('\n\n')
    ]


def solve(groups):
    return sum(
        len([
            c for c in CHAR_RANGE
            if all(c in passenger for passenger in group)
        ])
        for group in groups
    )


file_name = '6.txt'
groups = parse_input(file_name)
solution = solve(groups)
print(solution)
