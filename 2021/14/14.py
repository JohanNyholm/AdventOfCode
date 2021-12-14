from collections import defaultdict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f: 
        content = f.read()

    lines = content.split('\n')
    polymer = lines[0]

    rules = {
        pair: reaction
        for pair, reaction
        in (
            line.split(' -> ')
            for line in lines[2:]
        )
    }
    return polymer, rules


def step(pairs, rules):
    next_pairs = defaultdict(int)
    for react_pair, reaction in rules.items():
        if react_pair not in pairs:
            continue
        next_pairs[f"{react_pair[0]}{reaction}"] += pairs[react_pair]
        next_pairs[f"{reaction}{react_pair[1]}"] += pairs[react_pair]
    return next_pairs


def count_occurrances(pairs, head, tail):
    counts = defaultdict(int)
    for pair, num_pairs in pairs.items():
        counts[pair[0]] += num_pairs
        counts[pair[1]] += num_pairs

    # all units occurs in exactly two pairs except for the polymer head and tail
    # compensate, to support simple division by two later on
    counts[head] += 1
    counts[tail] += 1
    sorted_counts = sorted(val for val in counts.values())
    return (sorted_counts[-1] - sorted_counts[0]) // 2


def prep_structures(polymer):
    pairs = defaultdict(int)
    for m1, m2 in zip(polymer, polymer[1:]):
        pairs[f"{m1}{m2}"] += 1
    return pairs


def solve(polymer, rules, steps):
    pairs = prep_structures(polymer)
    for _ in range(steps):
        pairs = step(pairs, rules)
    solution = count_occurrances(pairs, polymer[0], polymer[-1])
    return solution


def main():
    polymer, rules = parse(INPUT_DIR / '14.txt')
    solution_a = solve(polymer, rules, 10)
    solution_b = solve(polymer, rules, 40)
    print(f"Solution a: {solution_a}")
    print(f"Solution b: {solution_b}")


if __name__ == '__main__':
    main()
