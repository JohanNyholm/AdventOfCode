from collections import defaultdict
import math

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

def vector_angle(from_, to_):
    from_x, from_y = from_
    to_x, to_y = to_
    delta_x = to_x - from_x
    delta_y = to_y - from_y
    angle = math.atan2(delta_x, delta_y)
    # angle = round(angle, 5)
    # print(angle)
    return angle
    
    # factor = delta_x**2 + delta_y**2
    # return (delta_x/factor, delta_y/factor)



def main():
    input_ = get_input('10.txt')
    print(input_)
    matrix = to_matrix(input_)
    print(matrix)
    
    max_asteroid = None
    max_detected = -1
    for asteroid in matrix:
        detected = set()
        angles = []
        for other_asteroid in matrix:
            if other_asteroid == asteroid:
                continue
            angle = vector_angle(asteroid, other_asteroid)
            if asteroid == (5, 8):
                angles.append(angle)
                # print(angle, other_asteroid)
            detected.add(angle)
            # for a in sorted(angles):
            #     print(a)
        # if asteroid == (5, 8):
        #     print(len(detected))
            # import pdb; pdb.set_trace()
        num_detected = len(detected)
        if num_detected > max_detected:
            max_detected = num_detected
            max_asteroid = asteroid
    print("RESULT")
    print(max_asteroid)
    print(max_detected)
main()