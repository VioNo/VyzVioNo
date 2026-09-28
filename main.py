from board import create_board, copy_board, print_board
from game import is_valid_move, make_move, is_win, find_tile
from input_handler import get_game_mode, get_tile
from computer import make_computer_move


def print_single_player(board, moves):
    """Вывод поля в одиночном режиме."""

    print_board(board)
    print(f"Количество ходов: {moves}")


def print_competition(
        player_board,
        computer_board,
        player_moves,
        computer_moves
):
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

        # Показываем текущее поле
        print_single_player(board, moves)

        # Проверяем победу
        if is_win(board):
            print("\nПОБЕДА!")
            print(
                f"Вы решили головоломку за {moves} ходов."
            )
            break

        # Получаем номер костяшки
        tile = get_tile()

        # Выход из игры
        if tile is None:
            print("\nИгра завершена.")
            break

        # Находим костяшку на поле
        position = find_tile(board, tile)

        if position is None:
            print("Ошибка: такая костяшка не найдена.")
            continue

        row, col = position

        # Проверяем возможность хода
        if not is_valid_move(board, row, col):
            print("Недопустимый ход!")
            print(
                f"Костяшка {tile} не находится рядом "
                "с пустой клеткой."
            )
            continue

        # Делаем ход
        make_move(board, row, col)
        moves += 1


def competition():
    """Игра против компьютера."""

    print("\nВы выбрали соревнование с компьютером.")

    # Создаём одно начальное поле
    original_board = create_board()

    # Игрок и компьютер получают одинаковое поле
    player_board = copy_board(original_board)
    computer_board = copy_board(original_board)

    player_moves = 0
    computer_moves = 0

    previous_computer_move = None

    while True:

        # Показываем оба поля
        print_competition(
            player_board,
            computer_board,
            player_moves,
            computer_moves
        )

        # ----------------------------
        # ХОД ИГРОКА
        # ----------------------------

        # Проверяем победу игрока
        if is_win(player_board):
            print("\nВЫ ПОБЕДИЛИ!")
            print(
                f"Вы собрали поле за "
                f"{player_moves} ходов."
            )
            print(
                f"Компьютер сделал "
                f"{computer_moves} ходов."
            )
            break

        # Получаем номер костяшки
        tile = get_tile()

        # Выход из игры
        if tile is None:
            print("\nИгра завершена.")
            break

        # Находим костяшку на поле игрока
        position = find_tile(player_board, tile)

        if position is None:
            print("Ошибка: такая костяшка не найдена.")
            continue

        row, col = position

        # Проверяем возможность хода
        if not is_valid_move(player_board, row, col):
            print("Недопустимый ход!")
            print(
                f"Костяшка {tile} не находится рядом "
                "с пустой клеткой."
            )
            continue

        # Игрок делает ход
        make_move(player_board, row, col)
        player_moves += 1

        # Проверяем победу игрока сразу после хода
        if is_win(player_board):
            print_competition(
                player_board,
                computer_board,
                player_moves,
                computer_moves
            )

            print("\nВЫ ПОБЕДИЛИ!")
            print(
                f"Вы собрали поле за "
                f"{player_moves} ходов."
            )
            break

        # ----------------------------
        # ХОД КОМПЬЮТЕРА
        # ----------------------------

        print("\nХод компьютера...")

        previous_computer_move = make_computer_move(
            computer_board,
            previous_computer_move
        )

        computer_moves += 1

        # Проверяем победу компьютера
        if is_win(computer_board):
            print_competition(
                player_board,
                computer_board,
                player_moves,
                computer_moves
            )

            print("\nКОМПЬЮТЕР ПОБЕДИЛ!")
            print(
                f"Компьютер собрал поле за "
                f"{computer_moves} ходов."
            )
            print(
                f"Вы сделали "
                f"{player_moves} ходов."
            )
            break

        # После хода компьютера снова показываем
        # оба поля перед следующим ходом игрока
        print_competition(
            player_board,
            computer_board,
            player_moves,
            computer_moves
        )


def main():
    print("========================================")
    print("          ИГРА «ПЯТНАШКИ»")
    print("========================================")
    print(
        "Правила: вы выбираете номер костяшки,\n"
        "которая будет перемещена на пустое место."
    )
    print("========================================")

    # Выбираем режим игры
    mode = get_game_mode()

    if mode == 1:
        single_player()
    else:
        competition()


if __name__ == "__main__":
    main()