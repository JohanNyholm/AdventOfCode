def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read()
        return lines.split('\n')

def fuel(mass):
    f = max((int(mass) // 3) - 2, 0)
    if f > 0:
        f = f + fuel(f)
    return f

modules = get_input('1.txt')
# fuel = 
print(sum(fuel(m) for m in modules))


module_max_len = Y
num modules = X

num_modules*(module_max_len/3)