import common


def parse_input(file_name):
    return common.get_int_input(file_name)


def solve(adapters):
    adapters = sorted(adapters)
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    diffs_1 = len([a for a, a_next in zip(adapters, adapters[1:]) if a + 1 == a_next])
    diffs_3 = len([a for a, a_next in zip(adapters, adapters[1:]) if a + 3 == a_next])
    return diffs_1 * diffs_3


file_name = '10.txt'
adapters = parse_input(file_name)
solution = solve(adapters)
print(solution)
