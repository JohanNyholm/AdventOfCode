from collections import deque
import pathlib
from functools import reduce


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'

CORRUPT_LINE_SCORE = -1


points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
chunk_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
chunk_openers = chunk_chars.keys()


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    return content.split('\n')


def solve_line(line):
    stack = deque()
    for char in line:
        if stack and char == chunk_chars[stack[-1]]:
            stack.pop()
        elif char in chunk_openers:
            stack.append(char)
        else:
            return CORRUPT_LINE_SCORE

    return reduce(
        (lambda acc, char: acc * 5 + points[chunk_chars[char]]),
        reversed(stack),
        0
    )


def solve(lines):
    solutions = (solve_line(line) for line in lines)
    solutions = [solution for solution in solutions if solution != CORRUPT_LINE_SCORE]
    return sorted(solutions)[len(solutions) // 2]


def main():
    lines = parse(INPUT_DIR / '10.txt')
    print("Solution:", solve(lines))


if __name__ == '__main__':
    main()
