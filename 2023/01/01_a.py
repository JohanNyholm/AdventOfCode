import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    return content.split('\n')


def main():
    items = parse(INPUT_DIR / '01_a.data')
    vals = []
    for row in items:
        first_val = next(v for v in row if '0' <= v <= '9')
        last_val = next(v for v in reversed(row) if '0' <= v <= '9')
        vals.append(int(f'{first_val}{last_val}'))
    print(sum(vals))

if __name__ == '__main__':
    main()
