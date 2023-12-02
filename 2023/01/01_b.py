import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def main():
    items = parse(INPUT_DIR / '01_b.data')
    vals = []
    digit_patterns = {
        'one': '1',
        '1': '1',
        'two': '2',
        '2': '2',
        'three': '3',
        '3': '3',
        'four': '4',
        '4': '4',
        'five': '5',
        '5': '5',
        'six': '6',
        '6': '6',
        'seven': '7',
        '7': '7',
        'eight': '8',
        '8': '8',
        'nine': '9',
        '9': '9',
    }
    for row in items:
        first_val = next(
            val
            for i in range(len(row))
            for val in (
                digit
                for digit_pattern, digit in digit_patterns.items()
                if row[i:].startswith(digit_pattern)
            )
        )
        last_val = next(
            val
            for i in reversed(range(len(row)))
            for val in (
                digit
                for spelling, digit in digit_patterns.items()
                if row[i:].startswith(spelling)
            )
        )
        vals.append(int(f'{first_val}{last_val}'))
    print(sum(vals))

if __name__ == '__main__':
    main()
