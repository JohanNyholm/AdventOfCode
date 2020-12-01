def get_input(fname):
    with open(f'input/{fname}', 'r') as f:
        lines = f.read()
        return lines


def chunks(list_, chunk_size):
    i = 0
    total_len = len(list_)
    num_chunks = total_len//chunk_size
    return [list_[start*chunk_size: end*chunk_size] for start, end in zip(range(num_chunks), range(1, num_chunks+1))]


def num_digits(list_, digit:int):
    digit = str(digit)
    return list_.count(digit)


def print_image(image, width, height):
    for h in range(height):
        row = []
        for pixel in image[width*h:width*(h+1)]:
            row.append({'0':'█', '1': ' '}[pixel])
        print(''.join(row))


def main():
    image_data = '0222112222120000'
    width = 2
    height = 2

    layers = chunks(image_data, width*height)
    rasterised_image = [next((d for d in digits if d != '2'), '2') for digits in zip(*layers)]
    print_image(rasterised_image, width, height)

main()
