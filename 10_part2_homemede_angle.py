from collections import defaultdict

def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read().split('\n')
        return lines


def to_matrix(input_):
    matrix = set()
    for y, line in enumerate(input_):
        for x, char in enumerate(line):
            if char == '#':
                matrix.add((x, y))
    return matrix


def clockwise_angle(from_, to_):
    from_x, from_y = from_
    to_x, to_y = to_
    delta_x = to_x - from_x
    delta_y = to_y - from_y
    dist = (delta_x**2 + delta_y**2)**0.5
    angle = -1
    if delta_x >= 0 and delta_y >= 0:
        angle = delta_x/dist
    elif delta_x >= 0 and delta_y <= 0:
        angle = abs(delta_y)/dist + 1
    elif delta_x <= 0 and delta_y <= 0:
        angle = abs(delta_x)/dist + 2
    elif delta_x <= 0 and delta_y >= 0:
        angle = delta_y/dist + 3
    else:
        raise Exception("Implementation error, uncaught angle: %d, %d", delta_x, delta_y)
    return angle


def dumb_dist(from_, to_):
    """
        some metric for comparing same angle vectors.
        calculating dumb_dist for two vectors with the same angle,
        the longer vector will have a larger dumb_dist
    """
    return abs(to_[0] - from_[0]) + abs(to_[0] - from_[0])


def main():
    input_ = get_input('10.txt')
    main_asteroid = (17, 23)
    AST_INDEX = 200
    # input_ = get_input('10_part2_test.txt')
    # main_asteroid = (8, 3)
    # AST_INDEX = 3
    print(input_)
    matrix = to_matrix(input_)
    print(matrix)
    
    def dumb_dist_to_main(asteroid):
        return dumb_dist(main_asteroid, asteroid)

    matrix.remove(main_asteroid)

    angles = defaultdict(set)
    for ast in matrix:
        angles[clockwise_angle(main_asteroid, ast)].add(ast)

    last_ast = None
    i = 0
    while(angles):
        for angle in sorted(angles.keys()):
            asteroids = angles[angle]
            min_dist_ast = min(asteroids, key=dumb_dist_to_main)
            last_ast = min_dist_ast
            i += 1
            if i == AST_INDEX:
                print("RESULT")
                print(last_ast)
                print(last_ast[0]*100 + last_ast[1])
                return
            asteroids.remove(min_dist_ast)
            if not asteroids:
                del angles[angle]
main()