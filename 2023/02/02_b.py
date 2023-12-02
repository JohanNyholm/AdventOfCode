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
    game_pattern = r'Game (?P<game_id>\d+): (?P<throws_str>.*)'
    game_re = re.compile(game_pattern)
    line_sum = 0
    for game_line in lines:
        limits = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        match = re.match(game_re, game_line)
        throws_str = match.group('throws_str')
        for throw in throws_str.split('; '):
            for color_pair in throw.split(', '):
                amount, color = color_pair.split(' ')
                amount = int(amount)
                limits[color] = max(amount, limits[color])
        line_sum += limits['blue']*limits['red']*limits['green']
    print(line_sum)

if __name__ == '__main__':
    main()
