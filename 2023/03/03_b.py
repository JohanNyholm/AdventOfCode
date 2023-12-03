import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse_lines(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def parse(file):
    possible_gears = set()
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
            if char == '*':
                possible_gears.add((x, y))
        if number:
            numbers[(x-len(number)+1, y)] = number
    return possible_gears, numbers


def main():
    possible_gears, numbers = parse(INPUT_DIR / '03.data')
    number_inverse_map = {}
    for (x, y), number in numbers.items():
        number_inverse_map.update(
            {(x_, y): (x, y) for x_ in range(x, x + len(number))}
        )
    gear_powers = []
    for (x, y) in possible_gears:
        adjacent_numbers = {
            number_inverse_map[(x_, y_)]
            for x_ in range(x - 1, x + 2)
            for y_ in range(y - 1, y + 2)
            if (x_, y_) in number_inverse_map
        }
        if len(adjacent_numbers) == 2:
            gear_powers.append(int(numbers[adjacent_numbers.pop()]) * int(numbers[adjacent_numbers.pop()]))
    print(sum(gear_powers))


if __name__ == '__main__':
    main()
