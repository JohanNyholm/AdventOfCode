import pathlib


ROOT_DIR = pathlib.Path(__file__).parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    move_lookup = {
        "forward": (1, 0),
        "down": (0, 1),
        "up": (0, -1),
    }
    def parse_move(move):
        (dir_, steps) = move.split(' ')
        steps = int(steps)
        return [v * steps for v in m[dir_]]

    return [parse_move(row) for row in content.split('\n')]


def main():
    moves = parse(INPUT_DIR / '02.txt')
    horizontal = sum(move[0] for move in moves)
    depth = sum(move[1] for move in moves)
    print(horizontal*depth)


if __name__ == '__main__':
    main()
