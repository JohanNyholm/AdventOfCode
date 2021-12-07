from collections import defaultdict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    return [int(v) for v in content.split(',')]


def solve(positions):
    with open('test.txt', 'w') as f:
        f.write(','.join(str(v) for v in sorted(positions)))
    min_pos = min(positions)
    max_pos = max(positions)
    acc_pos_costs = defaultdict(int)
    for position in positions:
        for x in range(min_pos, max_pos + 1):
            acc_pos_costs[x] += abs(x - position)

    min_pos = min(acc_pos_costs, key=acc_pos_costs.get)
    return min_pos


def main():
    positions = parse(INPUT_DIR / '07.txt')
    print("Solution:", solve(positions))


if __name__ == '__main__':
    main()
