import re
from functools import lru_cache

import common


def parse_input(file_name):
    return common.get_int_input(file_name)


def _get_first_invalid_number(numbers, window_size):
    def has_sum(val, window):
        for i, term1 in enumerate(window):
            for term2 in window[i+1:]:
                if term1 + term2 == val:
                    return True
        return False
    
    return next(
        val for i, val in enumerate(numbers[window_size:])
        if not has_sum(val, numbers[i: i + window_size])
    )


def _get_sum_range(numbers, invalid_number):
    number_len = len(numbers)
    for i in range(number_len - 1):
        j = next((
            j for j in range(i+2, number_len + 1)
            if sum(numbers[i: j]) >= invalid_number),
            number_len + 1
        )
        if sum(numbers[i: j]) == invalid_number:
            return max(numbers[i: j]) + min(numbers[i: j])


def solve(numbers, window_size):
    invalid_number = _get_first_invalid_number(numbers, window_size)
    with common.Timer('sum range'):
        return _get_sum_range(numbers, invalid_number)


file_name = '9.txt'
numbers = parse_input(file_name)
solution = solve(numbers, 25)
print(solution)
