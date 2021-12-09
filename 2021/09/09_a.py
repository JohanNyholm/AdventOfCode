from collections import defaultdict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    return [
        [int(c) for c in line]
        for line in content.split('\n')
    ]


def solve(matrix):
    x_len = len(matrix[0])
    y_len = len(matrix)
    
    def low_point_score(x, y):
        x_row = [matrix[y][x_] for x_ in range(max(0, x-1), min(x_len, x+2)) if x_ != x]
        y_row = [matrix[y_][x] for y_ in range(max(0, y-1), min(y_len, y+2)) if y_ != y]
        point_height = matrix[y][x]
        if point_height < min(x_row) and point_height < min(y_row):
            return point_height + 1
        return 0

    score = 0
    for y in range(y_len):
        for x in range(x_len):
            score += low_point_score(x, y)
    return score

def main():
    matrix = parse(INPUT_DIR / '09.txt')
    print("Solution:", solve(matrix))


if __name__ == '__main__':
    main()
