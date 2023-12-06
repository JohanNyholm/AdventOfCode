from collections import namedtuple
import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


SpecialEdge = namedtuple('SpecialEdge', [
    'dest_range_start',
    'source_range_start',
    'range_len'
])


Node = namedtuple('Node', [
    'type',
    'number',
])


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    chunks = [chunk.splitlines() for chunk in content.split('\n\n')]
    seeds = [int(seed.group(0)) for seed in re.finditer(r'\d+', chunks[0][0])]
    seeds = [
        (
            seeds[i],
            seeds[i+1]
        )
        for i in range(0, len(seeds), 2)
    ]
    special_directed_edges = {}
    for chunk_lines in chunks[1:]:
        match = re.match(
            r'(?P<destination>.+)-to-(?P<source>.+) map:',
            chunk_lines[0]
        )
        destination, source = match.groups()
        source_dest_special_edges = []
        for line in chunk_lines[1:]:
            match = re.match(
                r'(?P<source_range_start>\d+) (?P<dest_range_start>\d+) (?P<range_len>\d+)',
                line
            )
            source_dest_special_edges.append(
                SpecialEdge(
                    dest_range_start=int(match.group('dest_range_start')),
                    source_range_start=int(match.group('source_range_start')),
                    range_len=int(match.group('range_len')),
                )
            )
        special_directed_edges[source] = {
            'destination': destination,
            'edges': source_dest_special_edges,
        }
    return seeds, special_directed_edges


def solve(seeds, special_directed_edges):
    i = 0
    type = 'seed'
    while True:
        # if i % 100000 == 0:
        #     print(i)
        number = i
        type = 'location'
        while type != 'seed':
            edges = special_directed_edges[type]['edges']
            type = special_directed_edges[type]['destination']
            for edge in edges:
                if edge.source_range_start <= number < edge.source_range_start + edge.range_len:
                    diff = number - edge.source_range_start
                    number = edge.dest_range_start + diff
                    break
        for seed_range_start, range_len in seeds:
            if seed_range_start <= number < seed_range_start + range_len:
                print(i)
                return
        i += 1


def main():
    seeds, special_directed_edges = parse(INPUT_DIR / '05.data')
    solve(seeds, special_directed_edges)


if __name__ == '__main__':
    main()
