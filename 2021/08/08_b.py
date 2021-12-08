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


def solve_note(note):
    signals = note['digit_signals']
    output = note['output']

    combined_digits = ''.join(signals)
    frequencies = {
        char: sum(char == c for c in combined_digits)
        for char in 'abcdefg'
    }

    digit_1 = next(signal for signal in signals if len(signal) == 2)
    digit_4 = next(signal for signal in signals if len(signal) == 4)

    char_translation = {
        'a': next(char for char, freq in frequencies.items() if freq == 8 and char not in digit_1),
        'b': next(char for char, freq in frequencies.items() if freq == 6),
        'c': next(char for char, freq in frequencies.items() if freq == 8 and char in digit_1),
        'd': next(char for char, freq in frequencies.items() if freq == 7 and char in digit_4),
        'e': next(char for char, freq in frequencies.items() if freq == 4),
        'f': next(char for char, freq in frequencies.items() if freq == 9),
        'g': next(char for char, freq in frequencies.items() if freq == 7 and char not in digit_4),
    }
    char_reverse_lookup = {value: key for key, value in char_translation.items()}
    digits = {
        tuple('abcefg'): '0',
        tuple('cf'): '1',
        tuple('acdeg'): '2',
        tuple('acdfg'): '3',
        tuple('bcdf'): '4',
        tuple('abdfg'): '5',
        tuple('abdefg'): '6',
        tuple('acf'): '7',
        tuple('abcdefg'): '8',
        tuple('abcdfg'): '9',
    }

    digit = int("".join(
            digits[
                tuple(sorted(char_reverse_lookup[char] for char in signal))
            ] for signal in output
        )
    )
    return digit


def solve(notes):
    return sum(solve_note(note) for note in notes)


def main():
    notes = parse(INPUT_DIR / '08.txt')
    print("Solution:", solve(notes))


if __name__ == '__main__':
    main()
