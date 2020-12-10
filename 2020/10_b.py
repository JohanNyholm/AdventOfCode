from functools import lru_cache

import common


def parse_input(file_name):
    return common.get_int_input(file_name)


def solve(adapters):
    adapters = sorted(adapters)

    @lru_cache(maxsize=None)
    def count_combinations(i, jolt_target):
        if jolt_target <= 3:
            return 2**(i+1)
        if i < 0 or jolt_target - adapters[i] > 3:
            return 0
        return count_combinations(i-1, adapters[i]) + count_combinations(i-1, jolt_target)

    return count_combinations(
        i=len(adapters) - 1,
        jolt_target=max(adapters) + 3
    )


file_name = '10.txt'
adapters = parse_input(file_name)
with common.Timer():
    solution = solve(adapters)
print(solution)
