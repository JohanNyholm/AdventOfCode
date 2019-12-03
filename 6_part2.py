from collections import defaultdict
def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read()
        return [line.split(')') for line in lines.split('\n')]


def build_graph(edges):
    graph = defaultdict(set)
    san, you = None, None
    for from_, to in edges:
        if to == 'SAN':
            san = from_
            continue
        if to == 'YOU':
            you = from_
            continue
        graph[from_].add(to)
        graph[to].add(from_)
    return graph, you, san

def bfs(graph, you, san):
    distance = 0
    if you == san:
        return distance
    visited = set([you])
    to_visit = graph[you]
    while to_visit:
        next_level_visits = set()
        distance += 1
        visited.update(to_visit)
        for child in to_visit:
            # print(child)
            if child == san:
                return distance
            next_level_visits.update(graph[child])
        to_visit = next_level_visits.difference(visited)
    return -1

def main():
    edges = get_input('6_part2.txt')
    graph, you, san = build_graph(edges)
    print(bfs(graph, you, san))
main()