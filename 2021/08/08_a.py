from collections import defaultdict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    def parse_patterns(line):
        return line.strip().split(' ')

    return [
        {
            'digit_signals': parse_patterns(split_line[0]),
            'output': parse_patterns(split_line[1]),
        } for split_line in (line.split('|') for line in content.split('\n'))
    ]


def solve(notes):
    unique_lengths = set([2, 3, 4, 7])
    return sum(sum(len(signal) in unique_lengths for signal in note['output']) for note in notes)


def main():
    notes = parse(INPUT_DIR / '08.txt')
    print("Solution:", solve(notes))


if __name__ == '__main__':
    main()
