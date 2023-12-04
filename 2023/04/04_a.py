import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse_lines(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def main():
    sum_ = 0
    for line in parse_lines(INPUT_DIR / '04.data'):
        match = re.match(
            r'Card +\d+: (?P<winner_numbers>.+) \| (?P<my_numbers>.+)',
            line
        )
        winner_numbers = set([m.group(0) for m in re.finditer(r'(\d+)', match.group('winner_numbers'))])
        my_numbers = set([m.group(0) for m in re.finditer(r'(\d+)', match.group('my_numbers'))])
        num_corrects = len(winner_numbers & my_numbers)
        sum_ += num_corrects and 2**(num_corrects-1)
    print(sum_)


if __name__ == '__main__':
    main()
