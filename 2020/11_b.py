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
    y_len = len(seats)
    x_len = len(seats[0])

    def _direction_blocked(xd, yd):
        x_ = x + xd
        y_ = y + yd
        view_blocked = False
        while(0 <= y_ < y_len and 0 <= x_ < x_len):
            seat = seats[y_][x_]
            if seat == FLOOR:
                x_ += xd
                y_ += yd
                continue
            view_blocked = seat == OCCUPIED
            break
        return view_blocked

    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    return sum(_direction_blocked(xd, yd) for xd, yd in dirs)


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
            elif seat == OCCUPIED and num_adjacent >= 5:
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
