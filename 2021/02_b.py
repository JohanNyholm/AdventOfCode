import pathlib


ROOT_DIR = pathlib.Path(__file__).parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    aim_transform_lookup = {
        "forward": 0,
        "down": 1,
        "up": -1,
    }
    def parse_move(move):
        (dir_, x) = move.split(' ')
        x = int(x)

        def aim_transform(aim):
            return aim + (aim_transform_lookup[dir_] * x)

        def horizontal_transform(horizontal):
            if dir_ == 'forward':
                return horizontal + x
            return horizontal
        
        def depth_transform(depth, aim):
            if dir_ == 'forward':
                return depth + (aim * x)
            return depth

        return {
            'aim_transform': aim_transform,
            'horizontal_transform': horizontal_transform,
            'depth_transform': depth_transform,
        }

    return [parse_move(row) for row in content.split('\n')]


def main():
    moves = parse(INPUT_DIR / '02.txt')
    aim = 0
    depth = 0
    horizontal = 0
    for move in moves:
        aim = move['aim_transform'](aim)
        depth = move['depth_transform'](depth, aim)
        horizontal = move['horizontal_transform'](horizontal)

    print(depth * horizontal)


if __name__ == '__main__':
    main()
