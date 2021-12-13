from collections import namedtuple
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Point = namedtuple('Point', ['x', 'y'])

Fold = namedtuple('Fold', ['axis', 'index'])


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    point_lines, fold_lines = content.split('\n\n')
    points = set(
        Point(
            *(int(v) for v in row.split(','))
        ) for row in point_lines.split('\n')
    )
    
    def parse_fold(line):
        trimmed_line = "".join(line[len('fold along '):])
        axis, index = trimmed_line.split('=')
        return Fold(axis, int(index))
    
    folds = [parse_fold(line) for line in fold_lines.split('\n')]
    return points, folds


def print_points(points):
    y_max = max(point.y for point in points)
    x_max = max(point.x for point in points)
    print('-' * (x_max + 1))
    for y in range(0, y_max + 1):
        print("".join([
            '#' if Point(x, y) in points else '.' for x in range(0, x_max + 1)
        ]))
    print('-' * (x_max + 1))


def fold_point(point, fold):
    if fold.axis == 'x':
        return Point(
            fold.index - abs(point.x - fold.index),
            point.y
        )
    else:
        return Point(
            point.x,
            fold.index - abs(point.y - fold.index)
        )


def solve(points, folds):
    for fold in folds:
        points = set(fold_point(point, fold) for point in points)
    
    # outsourcing image processing
    print("Time to shine!")
    print_points(points)
    chars = input("what does it say?\n> ").strip()
    assert chars, "No shine!"
    return chars.upper()


def main():
    points, folds = parse(INPUT_DIR / '13.txt')
    solution = solve(points, folds)

    print("Solution:", solution)


if __name__ == '__main__':
    main()
