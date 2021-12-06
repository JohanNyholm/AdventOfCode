from collections import defaultdict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    return [int(v) for v in content.split(',')]


def count_fishes(fishes):
    return sum(num for num in fishes.values())


def new_day(fishes):
    new_fishes = defaultdict(int)
    for fish_timer, num_fishes in fishes.items():
        if fish_timer == 0:
            new_fishes[6] += num_fishes
            new_fishes[8] += num_fishes
        else:
            new_fishes[fish_timer - 1] += num_fishes
    return new_fishes


def solve(fishes, num_days):
    for _ in range(num_days):
        fishes = new_day(fishes)
    return count_fishes(fishes)


def main():
    fish_list = parse(INPUT_DIR / '06.txt')

    fishes = defaultdict(int)
    for fish in fish_list:
        fishes[fish] += 1

    print("Solution A:", solve(fishes, 80))
    print("Solution B:", solve(fishes, 256))


if __name__ == '__main__':
    main()
