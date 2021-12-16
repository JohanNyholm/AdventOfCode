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
    print_(f"literal: {int(literal, 2)}")


def parse_operator(iter_string):
    length_type_id = iter_string.take(1)
    if length_type_id == '0':
        sub_packages_length = int(iter_string.take(15), 2)
        # TODO! fix! hack!
        iter_start = iter_string.i
        while(iter_string.i - iter_start < sub_packages_length):
            parse_package(iter_string)
    else:
        num_sub_packages = int(iter_string.take(11), 2)
        for _ in range(num_sub_packages):
            parse_package(iter_string)


def parse_package(iter_string):
    # header
    version = iter_string.take(3)
    global version_count
    version_count += int(version, 2)
    type_ = iter_string.take(3)
    if type_ == '100':
        parse_literal(iter_string)
    else:
        parse_operator(iter_string)


def prep_structures(hexa_chars):
    return "".join(
        bin(int(char, 16))[2:].zfill(4)
        for char in hexa_chars
    )


def solve(hexa_chars):
    binary_string = prep_structures(hexa_chars)
    binary_string_iterator = IterStr(binary_string)
    print(binary_string)
    parse_package(binary_string_iterator)
    return version_count


def main():
    hexa_chars = parse(INPUT_DIR / '16.txt')
    with verbose_timer():
        solution = solve(hexa_chars)
    print(f"Solution: {solution}")


if __name__ == '__main__':
    main()
