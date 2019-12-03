from collections import defaultdict
import re

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
        # print(axis, axis_vel_delta)
        moon[f'v{axis}']+=axis_vel_delta


def gravity(moons):
    for axis in AXES:
        axis_gravity(moons, axis)


def velocity(moons):
    for moon in moons:
        for axis in AXES:
            axis_pos = moon[axis]
            axis_vel = moon[f'v{axis}']
            moon[axis] += axis_vel 

def time_step(moons):
    gravity(moons)
    velocity(moons)


def kinetic_energy(moons):
    total_kinetic = 0
    for moon in moons:
        pos_kin = 0
        vel_kin = 0
        for axis in AXES:
            pos_kin += abs(moon[axis])
        for axis in AXES:
            vel_kin += abs(moon[f'v{axis}'])
        total_kinetic += (pos_kin * vel_kin)
    return total_kinetic
            

def main():
    input_ = get_input('12.txt')
    moons = make_moons(input_)
    print_moons(moons)
    for i in range(1000):
        time_step(moons)
        # print(f'\nSTEP {i+1}')
        # print_moons(moons)
    print(kinetic_energy(moons))

main()