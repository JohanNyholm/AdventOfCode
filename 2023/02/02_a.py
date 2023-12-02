import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def main():
    lines = parse(INPUT_DIR / '02.data')
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    game_pattern = r'Game (?P<game_id>\d+): (?P<throws_str>.*)'
    game_re = re.compile(game_pattern)
    line_sum = 0
    for game_line in lines:
        match = re.match(game_re, game_line)
        game_id = int(match.group('game_id'))
        throws_str = match.group('throws_str')
        try:
            for throw in throws_str.split('; '):
                for color_pair in throw.split(', '):
                    amount, color = color_pair.split(' ')
                    amount = int(amount)
                    if amount > limits[color]:
                        raise ValueError()
        except ValueError:
            continue
        line_sum += game_id
            
    print(line_sum)

if __name__ == '__main__':
    main()
