from collections import defaultdict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    return [int(v) for v in content.split(',')]


def solve(positions):
    min_pos = min(positions)
    max_pos = max(positions)

    dist_move_costs = [0] * (max_pos - min_pos + 1)
    for i in range(1, len(dist_move_costs)):
        dist_move_costs[i] = dist_move_costs[i-1] + i

    acc_pos_costs = defaultdict(int)
    for position in positions:
        for x in range(min_pos, max_pos + 1):
            dist = abs(x - position)
            acc_pos_costs[x] += dist_move_costs[dist]

    min_pos = min(acc_pos_costs, key=acc_pos_costs.get)
    return min_pos


def main():
    positions = parse(INPUT_DIR / '07.txt')
    print("Solution:", solve(positions))


if __name__ == '__main__':
    main()
