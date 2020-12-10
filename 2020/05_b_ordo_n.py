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
    num_seats = len(seat_numbers) + 1
    min_seat = min(seat_numbers)
    occupied_seats = [False for _ in range(num_seats)]
    for seat_nbr in seat_numbers:
        occupied_seats[seat_nbr - min_seat] = True
    return occupied_seats.index(False) + min_seat


file_name = '05.txt'
seat_numbers = parse_input(file_name)
solution = solve(seat_numbers)
print(solution)
