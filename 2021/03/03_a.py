import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    def parse_binary_string(row):
        return [v == "1" for v in row]

    return [parse_binary_string(row) for row in content.split('\n')]


def bin_row_to_int(row):
    return int("".join("1" if v else "0" for v in row), 2)


def find_most_common_bit(rows, i):
    return sum(row[i] for row in rows) >= len(rows)/2


def main():
    rows = parse(INPUT_DIR / '03.txt')
    row_len = len(rows[0])
    most_common_bits = [
        find_most_common_bit(rows, i)
        for i in range(row_len)
    ]
    gamma = bin_row_to_int(most_common_bits)
    # invert the bit pattern to get epsillon
    epsillon = 2**row_len -1 - gamma
    print(gamma * epsillon)

        
if __name__ == '__main__':
    main()
