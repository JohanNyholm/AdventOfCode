import pathlib


ROOT_DIR = pathlib.Path(__file__).parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    return [int(row) for row in content.split('\n')]


def main():
    items = parse(INPUT_DIR / '01.txt')
    result = sum(1 if a < b else 0 for a, b in zip(items, items[3:]))
    print(result)

if __name__ == '__main__':
    main()
