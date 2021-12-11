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
        new_to_flash = set()
        for p in to_flash:
            for adj_p in adjacents[p]:
                if adj_p not in flashed:
                    new_lvl = levels[adj_p] + 1
                    if new_lvl == 10:
                        new_to_flash.add(adj_p)
                    levels[adj_p] = new_lvl
        to_flash = new_to_flash
    for point in flashed:
        levels[point] = 0
    return len(flashed)

    return flashes


def solve(matrix, steps):
    points, levels, adjacents = prep_structures(matrix)
    tot_flashes = 0
    for i in range(steps):
        flashes = step(points, levels, adjacents)
        tot_flashes += flashes
    return tot_flashes


def main():
    matrix = parse(INPUT_DIR / '11.txt')
    print("Solution:", solve(matrix, 100))


if __name__ == '__main__':
    main()
