import time


def get_input(file_name):
    with open(f'input/{file_name}', 'r') as f:
        return f.read()


def get_input_lines(file_name):
    return get_input(file_name).split('\n')


def get_int_input(file_name):
    return [int(v) for v in get_input_lines(file_name)]


class Timer:
    def __init__(self, name='execution', verbose=True, ms=True):
        self.t0 = None
        self.name = name
        self.verbose = verbose
        self.ms = ms
        self.ns_delta = -1

    def print(self):
        delta = self.ns_delta
        unit = 'ms' if self.ms else 'ns'
        if self.ms:
            delta/=10**6
        print(f'{self.name} took {delta} {unit}')

    def __enter__(self):
        self.t0 = time.perf_counter_ns()

    def __exit__(self, *args):
        self.t1 = time.perf_counter_ns()
        self.ns_delta = self.t1 - self.t0
        if self.verbose:
            self.print()