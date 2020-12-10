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


def solve(numbers, window_size):
    return _get_first_invalid_number(numbers, window_size)


file_name = '09.txt'
numbers = parse_input(file_name)
solution = solve(numbers, 25)
print(solution)
