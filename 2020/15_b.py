import common


def parse_input(file_name):
    return [int(v) for v in common.get_input(file_name).split(',')]


def solve(numbers, turns):
    last_spoken_lookup = {n:i+1 for i, n in enumerate(numbers[:-1])}
    prev_number = numbers[-1]
    for turn in range(len(numbers), turns):
        new_number = 0
        if prev_number in last_spoken_lookup:
            new_number = turn - last_spoken_lookup[prev_number]
        last_spoken_lookup[prev_number] = turn
        prev_number = new_number
    return prev_number


file_name = '15.txt'
numbers = parse_input(file_name)
with common.Timer():
    solution = solve(numbers, 30000000)
print(solution)
