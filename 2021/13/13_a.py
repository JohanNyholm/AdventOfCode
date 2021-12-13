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
    
    return len(points)


def main():
    points, folds = parse(INPUT_DIR / '13.txt')
    solution = solve(points, folds[:1])

    print("Solution:", solution)


if __name__ == '__main__':
    main()
