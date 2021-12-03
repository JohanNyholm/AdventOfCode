import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'


def parse(file):
    with open(file, 'r') as f:
        content = f.read()
    
    def parse_binary_string(row):
        return [v == "1" for v in row]

    return [parse_binary_string(row) for row in content.split('\n')]


def filter_til_one_remains(rows, least_common=False, i=0):
    if not rows:
        raise ValueError("No rows to filter")
    if len(rows) == 1:
        return rows[0]
    
    filter_ = find_most_common_bit(rows, i) ^ least_common
    return filter_til_one_remains(
        [row for row in rows if row[i] == filter_],
        least_common,
        i + 1
    )


def bin_row_to_int(row):
    return int("".join("1" if v else "0" for v in row), 2)


def find_most_common_bit(rows, i):
    return sum(row[i] for row in rows) >= len(rows)/2


def main():
    rows = parse(INPUT_DIR / '03.txt')
    ogr_row = filter_til_one_remains(rows)
    csr_row = filter_til_one_remains(rows, least_common=True)
    ogr = bin_row_to_int(ogr_row)
    csr = bin_row_to_int(csr_row)
    print(ogr * csr)  

        
if __name__ == '__main__':
    main()
