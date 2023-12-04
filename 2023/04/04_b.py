import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse_lines(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def main():
    total_cards = 0
    card_duplicators = []
    for line in parse_lines(INPUT_DIR / '04.data'):
        current_card_copies = 1 + sum(factor for _, factor in card_duplicators)
        total_cards += current_card_copies
        card_duplicators = [
            (remaining_rounds - 1, factor)
            for remaining_rounds, factor in card_duplicators
            if remaining_rounds > 1
        ]
        match = re.match(
            r'Card +\d+: (?P<winner_numbers>.+) \| (?P<my_numbers>.+)',
            line
        )
        winner_numbers = set([m.group(0) for m in re.finditer(r'(\d+)', match.group('winner_numbers'))])
        my_numbers = set([m.group(0) for m in re.finditer(r'(\d+)', match.group('my_numbers'))])
        num_correct = len(winner_numbers & my_numbers)
        if num_correct:
            card_duplicators.append((num_correct, current_card_copies))
    print(total_cards)


if __name__ == '__main__':
    main()
