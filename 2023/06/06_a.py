import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse_lines(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def main():
    lines = parse_lines(INPUT_DIR / '06.data')
    times = [int(m.group(0)) for m in re.finditer(r'(\d+)', lines[0])]
    distance_records = [int(m.group(0)) for m in re.finditer(r'(\d+)', lines[1])]
    product = 1
    for time, distance_record in zip(times, distance_records):
        product *= len(list(ct for ct in range(1, time) if (time-ct)*ct > distance_record))
    print(product)


if __name__ == '__main__':
    main()
