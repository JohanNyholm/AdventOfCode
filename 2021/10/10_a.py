from collections import deque
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
            # corrupt!!!!
            return points[char]
    return 0


def solve(lines):
    return sum(solve_line(line) for line in lines)


def main():
    lines = parse(INPUT_DIR / '10.txt')
    print("Solution:", solve(lines))


if __name__ == '__main__':
    main()
