import common


def parse_input(file_name):
    return [
        set(''.join(group.split('\n')))
        for group in common.get_input(file_name).split('\n\n')
    ]


def solve(groups):
    return sum(len(group) for group in groups)


file_name = '06.txt'
groups = parse_input(file_name)
solution = solve(groups)
print(solution)
