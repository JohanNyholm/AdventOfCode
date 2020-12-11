import common

FLOOR = -1
EMPTY = 0
OCCUPIED = 1


LINE_TRANSLATION = {
    'L': EMPTY,
    '.': FLOOR,
}
def parse_input(file_name):
    return [
        [LINE_TRANSLATION[c] for c in line]
        for line in common.get_input_lines(file_name)
    ]


def _adjacent_seats(seats, x, y):
    seat_val = seats[y][x]
    num = sum(
        sum(s for s in row[max(0, x-1): x+2] if s != FLOOR)
        for row in seats[max(0, y-1): y+2]
    ) - seat_val
    return num


def round(seats):
    new_seats = [row.copy() for row in seats]
    y_len = len(seats)
    x_len = len(seats[0])
    changed = False
    for y in range(y_len):
        for x in range(x_len):
            seat = seats[y][x]
            if seat == FLOOR:
                continue
            num_adjacent = _adjacent_seats(seats, x, y)
            if seat == EMPTY and num_adjacent == 0:
                changed = True
                new_seats[y][x] = OCCUPIED
            elif seat == OCCUPIED and num_adjacent >= 4:
                changed = True
                new_seats[y][x] = EMPTY
    return new_seats, changed


def _count_occupied(seats):
    return sum(sum(s == OCCUPIED for s in row) for row in seats)


def solve(seats):
    changed = True
    while changed:
        seats, changed = round(seats)
    return _count_occupied(seats)


file_name = '11.txt'
seats = parse_input(file_name)
solution = solve(seats)
print(solution)
