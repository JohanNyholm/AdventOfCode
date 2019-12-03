from collections import defaultdict
def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read()
        return [line.split(')') for line in lines.split('\n')]


def build_graph(directed_edges):
    graph = defaultdict(list)
    for from_, to in directed_edges:
        graph[from_].append(to)
    return graph

visited = set()
def orbits(graph, node):
    if node in visited:
        raise ValueError()
    visited.add(node)
    print(node)
    # if depth > 10:
    #     raise Exception()
    depth = 0
    total_orbits = depth
    to_visit = graph[node]
    while to_visit:
        next_level_visits = []
        depth += 1
        for child in to_visit:
            next_level_visits.extend(graph[child])
            total_orbits += depth
        to_visit = next_level_visits
    return total_orbits

def main():
    directed_edges = get_input('6.txt')
    graph = build_graph(directed_edges)
    # print(graph)
    print(orbits(graph, 'COM'))
    # for noun in range(100):
    #     for verb in range(100):
    #         if run(p, noun, verb) == 19690720:
    #             print(noun*100 + verb)
    #             return
main()