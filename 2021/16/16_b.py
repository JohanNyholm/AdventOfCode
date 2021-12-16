import functools
from collections import namedtuple
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


Point = namedtuple('Point', ['x', 'y'])


version_count = 0

def print_(message):
    print(message)


from time import perf_counter
class verbose_timer:
    def __init__(self, what='Execution'):
        self.what = what

    def __enter__(self):
        self.t1 = perf_counter()

    def __exit__(self, *argv):
        self.t2 = perf_counter()
        print(f"{self.what} took {self.t2-self.t1}s")


def parse(file):
    with open(file, 'r') as f: 
        content = f.read()

    return content


class IterStr:
    def __init__(self, str_):
        self.iter = iter(str_)
        self.str_ = str_
        self.i = 0
    
    def take(self, amount):
        i = self.i
        self.i += amount
        return self.str_[i: self.i]


def parse_literal(iter_string):
    group_type = '1'
    literal = ''
    while(group_type == '1'):
        group_type = iter_string.take(1)
        literal += iter_string.take(4)
    literal = int(literal, 2)
    print_(f"literal: {literal}")
    return literal


def parse_operator_operands(iter_string):
    length_type_id = iter_string.take(1)
    if length_type_id == '0':
        sub_packages_length = int(iter_string.take(15), 2)
        # TODO! fix! hack!
        iter_start = iter_string.i
        while(iter_string.i - iter_start < sub_packages_length):
            yield parse_package(iter_string)
    else:
        num_sub_packages = int(iter_string.take(11), 2)
        for _ in range(num_sub_packages):
            yield parse_package(iter_string)


def parse_package(iter_string) -> int:
    # header
    version = iter_string.take(3)
    global version_count
    version_count += int(version, 2)
    type_ = int(iter_string.take(3), 2)

    if type_ == 4:
        return parse_literal(iter_string)
    operands = list(parse_operator_operands(iter_string))
    match type_:
        case 0:
            return sum(operands)
        case 1:
            return functools.reduce(
                lambda prod, factor: prod * factor,
                operands
            )
        case 2:
            return min(operands)
        case 3:
            return max(operands)
        case 5:
            return operands[0] > operands[1]
        case 6:
            return operands[0] < operands[1]
        case 7:
            return operands[0] == operands[1]


def prep_structures(hexa_chars):
    return "".join(
        bin(int(char, 16))[2:].zfill(4)
        for char in hexa_chars
    )


def solve(hexa_chars):
    binary_string = prep_structures(hexa_chars)
    binary_string_iterator = IterStr(binary_string)
    print(binary_string)
    solution = parse_package(binary_string_iterator)
    return solution


def main():
    hexa_chars = parse(INPUT_DIR / '16.txt')
    with verbose_timer():
        solution = solve(hexa_chars)
    print(f"Solution: {solution}")


if __name__ == '__main__':
    main()
