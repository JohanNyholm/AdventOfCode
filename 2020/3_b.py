import common


def parse_input(file_name):
    return [[1 if v == '#' else 0 for v in line] for line in common.get_input(file_name)]


def solve(grid, dx, dy):
    y_max = len(grid)
    x_max = len(grid[0])
    return sum(grid[y][(i*dx) % x_max] for i, y in enumerate(range(0, y_max, dy)))


file_name = '3.txt'
grid = parse_input(file_name)
directions = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
product = 1
for dx, dy in directions:
    solution = solve(grid, dx, dy)
    product *= solution
print(product)
