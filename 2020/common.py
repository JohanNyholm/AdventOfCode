def get_input_lines(file_name):
    with open(f'input/{file_name}', 'r') as f:
        lines = f.read()
        return lines.split('\n')


def get_int_input(file_name):
    return [int(v) for v in get_input_lines(file_name)]
