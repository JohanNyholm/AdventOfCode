from collections import defaultdict
import re
import copy

AXES = ['x', 'y', 'z']


def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read().split('\n')
        return lines


def make_moons(rows):
    moons = []
    for row in rows:
        match = re.match('<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', row)
        x, y, z = (int(v) for v in match.groups())
        moons.append({'x': x, 'y': y, 'z': z, 'vx': 0, 'vy': 0, 'vz': 0})
    return moons


def print_moons(moons):
    for moon in moons:
        print(moon)


def axis_gravity(moons, axis):
    for moon in moons:
        axis_vel_delta = 0
        axis_pos = moon[axis]
        for other_moon in moons:
            if other_moon == moon:
                continue
            other_axis_pos = other_moon[axis]
            if other_axis_pos > axis_pos:
                axis_vel_delta += 1
            elif other_axis_pos < axis_pos:
                axis_vel_delta -= 1
        moon[f'v{axis}']+=axis_vel_delta


def axis_velocity(moons, axis):
    for moon in moons:
        axis_pos = moon[axis]
        axis_vel = moon[f'v{axis}']
        moon[axis] += axis_vel 


def axis_time_step(moons, axis):
    axis_gravity(moons, axis)
    axis_velocity(moons, axis)


def axis_moons_id(moons, axis):
    parts = []
    for moon in moons:
        parts.append(moon[axis])
        parts.append(moon[f'v{axis}'])
    return '_'.join((str(p) for p in parts))


def axis_period(moons, axis):
    moons = copy.deepcopy(moons)
    states = set()
    m_id = axis_moons_id(moons, axis)
    states.add(m_id)
    for i in range(1000000):
        axis_time_step(moons, axis)
        m_id = axis_moons_id(moons, axis)
        if m_id in states:
            return i + 1
        states.add(m_id)
    else:
        raise Exception('Failed')


def lcm(a, b):
    import math
    return abs(a*b) // math.gcd(a, b)


def main():
    input_ = get_input('12.txt')
    moons = make_moons(input_)
    periods = [axis_period(moons, axis) for axis in AXES]
    print(periods)
    print(lcm(periods[0], lcm(periods[1], periods[2])))

main()