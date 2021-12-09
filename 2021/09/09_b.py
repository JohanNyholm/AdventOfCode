from collections import namedtuple
import pathlib
from functools import reduce


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Point = namedtuple('Point', ['x', 'y'])


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    return [
        [int(c) for c in line]
        for line in content.split('\n')
    ]


def collect_basin_point(point, not_collected, basin):
    basin.add(point)
    x, y = point
    not_collected.remove(point)
    for adjacent_point in (
        Point(x - 1, y),
        Point(x + 1, y),
        Point(x, y - 1),
        Point(x, y + 1),
    ):
        if adjacent_point in not_collected:
            collect_basin_point(adjacent_point, not_collected, basin)


def solve(matrix):
    not_collected = set(
        Point(x, y)
        for y, row in enumerate(matrix)
        for x, depth in enumerate(row)
        if depth != 9
    )
    basins = []
    while not_collected:
        basin = set()
        collect_basin_point(
            next(iter(not_collected)),
            not_collected,
            basin
        )
        basins.append(basin)

    top_basin_size_product = reduce(
        lambda product, size: product * size,
        sorted(
            [len(basin) for basin in basins],
            reverse=True
        )[:3]
    )
    return top_basin_size_product


def main():
    matrix = parse(INPUT_DIR / '09.txt')
    from time import perf_counter
    t1 = perf_counter()
    solution = solve(matrix)
    t2 = perf_counter()
    print(f" {t2-t1}s")
    print("Solution:", solve(matrix))


if __name__ == '__main__':
    main()
