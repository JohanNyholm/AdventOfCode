import common


def solve_2(numbers, target_sum):
    half = target_sum / 2
    entry1 = next((n for n in numbers if (target_sum-n) in numbers and n != half), None)
    entry2 = (target_sum - entry1) if entry1 is not None else None
    return entry1, entry2


def solve_3(numbers, target_sum):
    all_numbers = numbers
    numbers = numbers.copy()
    for entry1 in all_numbers:
        numbers.remove(entry1)
        entry2, entry3 = solve_2(numbers, target_sum - entry1)
        if None not in (entry2, entry3):
            return entry1, entry2, entry3
        numbers.add(entry1)
    return None, None, None


file_name = '1.txt'
target_sum = 2020
number_list = common.get_int_input(file_name)
numbers = set(number_list)
if len(number_list) > len(numbers):
    raise Exception("Current implementation can not handle duplicates")
entry1, entry2, entry3 = solve_3(numbers, target_sum)
product = entry1 * entry2 * entry3
print(product)
