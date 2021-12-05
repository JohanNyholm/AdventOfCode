import pathlib
from collections import namedtuple, defaultdict


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['p1', 'p2'])


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    def parse_point(line):
        return Point(*(int(v) for v in line.split(',')))
    
    def parse_line(line):
        return Line(*(parse_point(p_str) for p_str in line.split(' -> ')))

    return [parse_line(line) for line in content.split('\n')]


def solve(lines):
    
    def is_valid_line(line):
        p1, p2 = line
        return (
            p1.x == p2.x
            or p1.y == p2.y 
            or (abs(p1.x - p2.x) == abs(p1.y - p2.y))
        )

    def points(from_: Point, to: Point):
        x_delta = to.x - from_.x
        y_delta = to.y - from_.y
        line_length = max(abs(x_delta), abs(y_delta))
        yield from (
            Point(
                from_.x + (x_delta//line_length) * i,
                from_.y + (y_delta//line_length) * i
            )
            for i in range(line_length + 1)
        )

    lines = [
        line for line in lines
        if is_valid_line(line)
    ]

    covered_area = defaultdict(int)
    for line in lines:
        for point in points(line.p1, line.p2):
            covered_area[point] += 1
    return len([1 for num_lines in covered_area.values() if num_lines > 1])
    

def main():
    lines = parse(INPUT_DIR / '05.txt')
    solution = solve(lines)
    print(solution)


if __name__ == '__main__':
    main()
