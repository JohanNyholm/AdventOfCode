from collections import defaultdict
def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read()
        return lines


def chunks(list_, chunk_size):
    i = 0
    total_len = len(list_)
    print (total_len, chunk_size)
    num_chunks = total_len//chunk_size
    # import pdb; pdb.set_trace()
    return [list_[start*chunk_size: end*chunk_size] for start, end in zip(range(num_chunks), range(1, num_chunks+1))]

def num_digits(list_, digit:int):
    digit = str(digit)
    return list_.count(digit)

def main():
    image_data = get_input('8.txt')
    width = 25
    height = 6
    
    # image_data = get_input('8_test.txt')
    # print(image_data)
    # width = 3
    # height = 2

    layers = chunks(image_data, width*height)
    least_zeroes_layer = min(layers, key=lambda l: num_digits(l, 0))
    num_1s = num_digits(least_zeroes_layer, 1)
    num_2s = num_digits(least_zeroes_layer, 2)
    print(num_1s*num_2s)
main()