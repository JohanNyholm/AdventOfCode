p = "146810-612564"
def criteria(num_string):
    if not len(num_string) == 6:
        return False
    has_pair = False
    for first, second in zip(num_string, num_string[1:]):
        if first > second:
            return False
        if first == second:
            has_pair = True
    return has_pair


(min_range_str, max_range_str) = p.split("-")
min_range, max_range = int(min_range_str), int(max_range_str)
valids = set()
for num in range(min_range, max_range+1):
    if criteria(str(num)):
        valids.add(num)
print(len(valids))
# print(criteria("212331"))