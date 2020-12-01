def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read()
        return lines.split('\n')


modules = get_input('1.txt')
print(sum((int(m) //3) - 2 for m in modules))