import common


def solve_2(numbers, target_sum):
    half = target_sum / 2
    entry1 = next((n for n in numbers if (target_sum-n) in numbers and n != half), None)
    entry2 = (target_sum - entry1) if entry1 is not None else None
    return entry1, entry2


file_name = '01.txt'
target_sum = 2020
number_list = common.get_int_input(file_name)
numbers = set(number_list)
if len(number_list) > len(numbers):
    raise Exception("Current implementation can not handle duplicates")
entry1, entry2 = solve_2(numbers, target_sum)
product = entry1 * entry2
print(product)
