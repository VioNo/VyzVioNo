import random

SIZE = 4


def is_solvable(board):
    """Проверяет, является ли позиция решаемой."""
    numbers = []

    for row in board:
        for tile in row:
            if tile != 0:
                numbers.append(tile)

    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    # Номер строки пустой клетки снизу: 1..4
    empty_row = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                empty_row = SIZE - i
                break

    if empty_row % 2 == 0:
        return inversions % 2 == 1

    return inversions % 2 == 0


def create_board():
    """Создаёт случайное решаемое поле."""
    numbers = list(range(1, 16)) + [0]

    while True:
        random.shuffle(numbers)

        board = [
            numbers[i:i + SIZE]
            for i in range(0, len(numbers), SIZE)
        ]

        if is_solvable(board):
            return board


def copy_board(board):
    """Создаёт копию игрового поля."""
    return [row[:] for row in board]


def print_board(board, title="Игровое поле"):
    """Выводит поле."""
    print(title)
    print("+----+----+----+----+")

    for row in board:
        for tile in row:
            if tile == 0:
                print("|    ", end="")
            else:
                print(f"| {tile:2} ", end="")

        print("|")
        print("+----+----+----+----+")