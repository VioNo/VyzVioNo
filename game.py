SIZE = 4


def find_empty(board):
    """Находит пустую клетку."""
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                return row, col

    return None

def find_tile(board, tile):
    """Находит координаты указанной костяшки."""

    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == tile:
                return row, col

    return None


def is_valid_move(board, row, col):
    """Проверяет возможность хода."""
    empty = find_empty(board)

    if empty is None:
        return False

    empty_row, empty_col = empty

    return abs(row - empty_row) + abs(col - empty_col) == 1


def make_move(board, row, col):
    """Перемещает костяшку."""
    empty_row, empty_col = find_empty(board)

    board[empty_row][empty_col], board[row][col] = (
        board[row][col],
        board[empty_row][empty_col]
    )


def is_win(board):
    """Проверяет, собрано ли поле."""
    expected = list(range(1, 16)) + [0]

    current = []

    for row in board:
        current.extend(row)

    return current == expected