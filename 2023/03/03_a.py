import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse_lines(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def parse(file):
    symbols = set()
    numbers = {}
    for y, line in enumerate(parse_lines(file)):
        number = ''
        for x, char in enumerate(line):
            if '0' <= char <= '9':
                number += char
                continue
            if number:
                numbers[(x-len(number), y)] = number
                number = ''
            if char != '.':
                symbols.add((x, y))
        if number:
            numbers[(x-len(number)+1, y)] = number
    return symbols, numbers


def main():
    symbols, numbers = parse(INPUT_DIR / '03.data')
    adjacent_numbers = []
    for (x, y), number in numbers.items():
        if any(
            (x_, y_) in symbols
            for x_ in range(x - 1, x + len(number) + 1)
            for y_ in range(y - 1, y + 2)
        ):
            adjacent_numbers.append(int(number))
    print(sum(adjacent_numbers))


if __name__ == '__main__':
    main()
