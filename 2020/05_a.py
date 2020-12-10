import common


def parse_input(file_name):
    lookup = {
        'B': '1',
        'F': '0',
        'R': '1',
        'L': '0',
    }
    return [
        int(''.join(lookup[c] for c in line), 2)
        for line in common.get_input_lines(file_name)
    ]


def solve(seat_numbers):
    return max(seat_numbers)


file_name = '5.txt'
seat_numbers = parse_input(file_name)
solution = solve(seat_numbers)
print(solution)
