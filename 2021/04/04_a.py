import pathlib


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / 'input'

EMPTY_SET = set()
BOARD_SIZE = 5


def parse(file):
    with open(file, 'r') as f:
        content = f.read()

    boards = content.split('\n\n')
    draws = boards.pop(0)  # first is not a board ;)
    draws = [int(v) for v in draws.split(',')]
    boards = [
        [
            [
                int(v) for v in row.split(' ') if v
            ] for row in
            board.split('\n')
        ] for board in boards
    ]
    return draws, boards


def invert_board(board):
    return [
        [row[i] for row in board]
        for i in range(BOARD_SIZE)
    ]


def settify_board(board):
    return {
        'cols': [set(row) for row in invert_board(board)],
        'rows': [set(row) for row in board],
    }


def solve(draws, boards):
    def is_winner(board):
        return EMPTY_SET in board['cols'] + board['rows']

    while True:
        draw = draws.pop(0)

        for board in boards:
            for row in board['cols'] + board['rows']:
                row.discard(draw)

        for board in boards:
            if is_winner(board):
                return sum(
                    sum(row)
                    for row in board['cols']  # can collect from either rows or cols, same thing
                ) * draw


def main():
    draws, boards = parse(INPUT_DIR / '04.txt')
    boards = [settify_board(board) for board in boards]
    solution = solve(draws, boards)
    print(solution)


if __name__ == '__main__':
    main()
