from collections import defaultdict, namedtuple
import pathlib


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

    def count_paths_to_end(visited, cave):
        if cave == END:
            return 1

        visited = visited.union({cave})
        return sum(
            count_paths_to_end(visited, connected_cave)
            for connected_cave in connections[cave]
            if connected_cave in multivisit_caves or connected_cave not in visited
        )      

    num_paths = count_paths_to_end(set(), START)
    return num_paths


def main():
    edges = parse(INPUT_DIR / '12.txt')
    print("Solution:", solve(edges))


if __name__ == '__main__':
    main()
