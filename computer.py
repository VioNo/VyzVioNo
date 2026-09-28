from game import find_empty, make_move, is_win


SIZE = 4


def manhattan_distance(board):
    """
    Считает, насколько костяшки далеко
    от своих правильных позиций.
    """
    distance = 0

    for row in range(SIZE):
        for col in range(SIZE):
            value = board[row][col]

            if value == 0:
                continue

            target_row = (value - 1) // SIZE
            target_col = (value - 1) % SIZE

            distance += abs(row - target_row)
            distance += abs(col - target_col)

    return distance


def get_possible_moves(board):
    """Возвращает все возможные ходы компьютера."""
    empty_row, empty_col = find_empty(board)

    possible_moves = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:
        row = empty_row + dr
        col = empty_col + dc

        if 0 <= row < SIZE and 0 <= col < SIZE:
            possible_moves.append((row, col))

    return possible_moves


def copy_board(board):
    """Создаёт копию поля."""
    return [row[:] for row in board]


def get_computer_move(board, previous_move=None):
    """
    Выбирает лучший ход компьютера.
    Компьютер старается уменьшить Manhattan distance.
    """

    possible_moves = get_possible_moves(board)

    # Если есть несколько вариантов,
    # стараемся не делать ход назад.
    if previous_move is not None and len(possible_moves) > 1:
        filtered_moves = [
            move for move in possible_moves
            if move != previous_move
        ]

        if filtered_moves:
            possible_moves = filtered_moves

    best_move = None
    best_score = float("inf")

    for move in possible_moves:
        test_board = copy_board(board)

        make_move(test_board, move[0], move[1])

        score = manhattan_distance(test_board)

        # Если компьютер уже выиграл,
        # это максимально хороший ход.
        if is_win(test_board):
            return move

        if score < best_score:
            best_score = score
            best_move = move

    return best_move


def make_computer_move(board, previous_move=None):
    """
    Делает один ход компьютера.
    Возвращает координаты передвинутой костяшки.
    """

    move = get_computer_move(board, previous_move)

    if move is not None:
        make_move(board, move[0], move[1])

    return move