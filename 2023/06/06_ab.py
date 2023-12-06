import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    return content


def main():
    content = parse(INPUT_DIR / '06.data')
    time, distance_record = [int(m.group()) for m in re.finditer(r'(\d+)', content.replace(' ', ''))]
    result = len(list(ct for ct in range(1, time) if (time-ct)*ct > distance_record))
    print(result)


if __name__ == '__main__':
    main()
