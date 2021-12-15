from collections import namedtuple
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Point = namedtuple('Point', ['x', 'y'])


from time import perf_counter
class verbose_timer:
    def __init__(self, what='Execution'):
        self.what = what

    def __enter__(self):
        self.t1 = perf_counter()

    def __exit__(self, *argv):
        self.t2 = perf_counter()
        print(f"{self.what} took {self.t2-self.t1}s")


def parse(file):
    with open(file, 'r') as f: 
        content = f.read()

    matrix = [[int(v) for v in row] for row in content.split('\n')]
    return matrix


def prep_structures(matrix, scale):
    graph = {}
    risk_levels = {}
    points = set()
    col_len = len(matrix)
    for y, row in enumerate(matrix):
        row_len = len(row)
        for x, level in enumerate(row):
            # scale it up
            for x_i in range(scale):
                for y_i in range(scale):
                    p = Point(x + x_i * row_len, y + y_i * col_len)
                    points.add(p)
                    risk_levels[p] =  (level - 1 + (x_i + y_i)) % 9 + 1

    for point in points:
        x, y = point
        graph[point] = set(
            p for p in 
            (
                Point(x - 1, y),
                Point(x + 1, y),
                Point(x, y - 1),
                Point(x, y + 1),
            ) if p in points
        )
    return graph, risk_levels


def solve(matrix, scale):
    graph, risk_levels = prep_structures(matrix, scale)
    start = min(graph.keys())
    end = max(graph.keys())
    path_state = {
        start: 0
    }
    flow = 0
    visited = set([start])
    while end not in path_state:
        next_path_state = {}
        flow += 1
        for current_point, total_risk in path_state.items():
            not_visited = [point for point in graph[current_point] if point not in visited]
            if not_visited:
                # keep point until all its adjacent points have been visited
                next_path_state[current_point] = total_risk
            for point in not_visited:
                new_tot_risk = total_risk + risk_levels[point]
                if new_tot_risk <= flow:
                    visited.add(point)
                    next_path_state[point] = new_tot_risk
        path_state = next_path_state
    return flow


def main():
    matrix = parse(INPUT_DIR / '15.txt')
    with verbose_timer('A'):
        solution_a = solve(matrix, scale=1)
    with verbose_timer('B'):
        solution_b = solve(matrix, scale=5)
    print(f"Solution A: {solution_a}")
    print(f"Solution B: {solution_b}")


if __name__ == '__main__':
    main()
