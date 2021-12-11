from collections import namedtuple
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Point = namedtuple('Point', ['x', 'y'])


def print_board(matrix, levels):
    for y, row in enumerate(matrix):
        print("".join(str(levels[Point(x, y)]) for x, level in enumerate(row)))


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    return [[int(v) for v in row] for row in content.split('\n')]



def prep_structures(matrix):
    levels = {}
    points = set()
    adjacents = {}
    for y, row in enumerate(matrix):
        for x, level in enumerate(row):
            p = Point(x, y)
            points.add(p)
            levels[p] = level
    for point in points:
        adjacents[point] = set(
            p for p in 
            (
                Point(x, y)
                for x in range(point.x - 1, point.x + 2)
                for y in range(point.y - 1, point.y + 2)
            ) if p in points and p != point 
        )
    return points, levels, adjacents


def step(points, levels, adjacents):
    for point in points:
        levels[point] += 1

    flashed = set()
    to_flash = set(p for p in points if levels[p] > 9)
    while to_flash:
        flashed.update(to_flash)
        next_to_flash = set()
        for p in to_flash:
            for adj_p in adjacents[p]:
                if adj_p not in flashed:
                    new_lvl = levels[adj_p] + 1
                    if new_lvl == 10:
                        next_to_flash.add(adj_p)
                    levels[adj_p] = new_lvl
        to_flash = next_to_flash
    for point in flashed:
        levels[point] = 0
    return len(flashed)

    return flashes


def solve(matrix):
    points, levels, adjacents = prep_structures(matrix)
    num_points = len(points)
    tot_flashes = 0
    num_flashes = 0
    num_step = 0
    while num_flashes != num_points:
        num_flashes = step(points, levels, adjacents)
        num_step += 1

    return num_step


def main():
    matrix = parse(INPUT_DIR / '11.txt')
    from time import perf_counter
    t1 = perf_counter()
    solution = solve(matrix)
    t2 = perf_counter()
    print(f" {t2-t1}s")
    print("Solution:", solve(matrix))


if __name__ == '__main__':
    main()
