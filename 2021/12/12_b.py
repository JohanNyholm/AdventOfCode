from collections import defaultdict, namedtuple
import pathlib
from functools import lru_cache


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Edge = namedtuple('Edge', ['p1', 'p2'])

Cave = namedtuple('Cave', ['id', 'multivisit'])

START = 'start'
END = 'end'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    return set(Edge(*row.split('-')) for row in content.split('\n'))


def build_graph(edges):
    connections = defaultdict(set)
    multivisit_caves = set()
    for p1, p2 in edges:
        connections[p1].add(p2)
        connections[p2].add(p1)
        for p in (p1, p2):
            if p.upper() == p:
                multivisit_caves.add(p)
    return connections, multivisit_caves
    

def solve(edges):
    connections, multivisit_caves = build_graph(edges)

    @lru_cache(maxsize=None)
    def count_connected_paths_to_end(visited, cave, dual_visit_cave):
        return sum(
            count_paths_to_end(visited, connected_cave, dual_visit_cave=dual_visit_cave)
            for connected_cave in connections[cave]
            if connected_cave in multivisit_caves or connected_cave not in visited
        )

    @lru_cache(maxsize=None)
    def count_paths_to_end(visited, cave, dual_visit_cave):
        if cave == END:
            if dual_visit_cave is not None and dual_visit_cave not in visited:
                # This path did not use it's dual visit superpower and is thus a duplicate
                return 0
            return 1

        num_paths = count_connected_paths_to_end(visited.union({cave}), cave, dual_visit_cave)
        if cave not in multivisit_caves and cave != START and dual_visit_cave is None:
            num_paths += count_connected_paths_to_end(visited, cave, dual_visit_cave=cave)
        return num_paths

    num_paths = count_paths_to_end(frozenset(), START, dual_visit_cave=None)
    return num_paths


def main():
    edges = parse(INPUT_DIR / '12.txt')
    from time import perf_counter
    t1 = perf_counter()
    solution = solve(edges)
    t2 = perf_counter()
    print(f" {t2-t1}s")
    print("Solution:", solution)


if __name__ == '__main__':
    main()
