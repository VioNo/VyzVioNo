from board import create_board, copy_board, print_board
from game import is_valid_move, make_move, is_win
from input_handler import get_game_mode, get_coordinates
from computer import make_computer_move


def print_single_player(board, moves):
    """Вывод поля в одиночном режиме."""
    print_board(board)
    print(f"Количество ходов: {moves}")


def print_competition(player_board, computer_board,
                      player_moves, computer_moves):
    """Выводит оба поля в режиме соревнования."""

    print("\n" + "=" * 45)
    print("                 ВЫ")
    print("=" * 45)

    print_board(player_board, "Ваше поле:")
    print(f"Ваши ходы: {player_moves}")

    print("\n" + "=" * 45)
    print("             КОМПЬЮТЕР")
    print("=" * 45)

    print_board(computer_board, "Поле компьютера:")
    print(f"Ходы компьютера: {computer_moves}")


def single_player():
    """Обычная игра против самого себя."""

    print("\nВы выбрали одиночную игру.")

    board = create_board()
    moves = 0

    while True:
        print_single_player(board, moves)

        if is_win(board):
            print("\n ПОБЕДА!")
            print(f"Вы решили головоломку за {moves} ходов.")
            break

        coordinates = get_coordinates()

        if coordinates is None:
            print("\nИгра завершена.")
            break

        row, col = coordinates

        if board[row][col] == 0:
            print("Ошибка: выбрана пустая клетка.")
            continue

        if not is_valid_move(board, row, col):
            print("Недопустимый ход!")
            print(
                "Костяшка должна находиться рядом "
                "с пустой клеткой."
            )
            continue

        make_move(board, row, col)
        moves += 1


def competition():
    """Игра против компьютера."""

    print("\nВы выбрали соревнование с компьютером.")

    # Создаём одно начальное поле
    original_board = create_board()

    # У игрока и компьютера одинаковое начальное состояние
    player_board = copy_board(original_board)
    computer_board = copy_board(original_board)

    player_moves = 0
    computer_moves = 0

    previous_computer_move = None

    while True:
        print_competition(
            player_board,
            computer_board,
            player_moves,
            computer_moves
        )

        # ----------------------------
        # ХОД ИГРОКА
        # ----------------------------

        if is_win(player_board):
            print("\n ВЫ ПОБЕДИЛИ!")
            print(
                f"Вы собрали поле за {player_moves} ходов."
            )
            print(
                f"Компьютер сделал {computer_moves} ходов."
            )
            break

        coordinates = get_coordinates()

        if coordinates is None:
            print("\nИгра завершена.")
            break

        row, col = coordinates

        if player_board[row][col] == 0:
            print("Ошибка: выбрана пустая клетка.")
            continue

        if not is_valid_move(player_board, row, col):
            print("Недопустимый ход!")
            print(
                "Костяшка должна находиться рядом "
                "с пустой клеткой."
            )
            continue

        # Игрок делает ход
        make_move(player_board, row, col)
        player_moves += 1

        # Проверяем победу игрока сразу
        if is_win(player_board):
            print_competition(
                player_board,
                computer_board,
                player_moves,
                computer_moves
            )

            print("\n ВЫ ПОБЕДИЛИ!")
            print(
                f"Вы собрали поле за {player_moves} ходов."
            )
            break

        # ----------------------------
        # ХОД КОМПЬЮТЕРА
        # ----------------------------

        print("\n Ход компьютера...")

        previous_computer_move = make_computer_move(
            computer_board,
            previous_computer_move
        )

        computer_moves += 1

        # Показываем действие компьютера
        print("\nКомпьютер сделал ход:")

        print_board(
            computer_board,
            "Поле компьютера:"
        )

        print(
            f"Ходов компьютера: {computer_moves}"
        )

        # Проверяем победу компьютера
        if is_win(computer_board):
            print("\n КОМПЬЮТЕР ПОБЕДИЛ!")
            print(
                f"Компьютер собрал поле "
                f"за {computer_moves} ходов."
            )
            print(
                f"Вы сделали {player_moves} ходов."
            )
            break


def main():
    print("========================================")
    print("          ИГРА «ПЯТНАШКИ»")
    print(f"правила: вы выбираете костяшку, \nкоторая будет перемещена на пустое место")
    print("========================================")

    mode = get_game_mode()

    if mode == 1:
        single_player()
    else:
        competition()


if __name__ == "__main__":
    main()