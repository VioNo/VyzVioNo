def get_game_mode():
    """Выбирает режим игры."""

    while True:
        print("\nВыберите режим игры:")
        print("1 — играть в одиночку")
        print("2 — играть против компьютера")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            return 1

        if choice == "2":
            return 2

        print("Ошибка: введите 1 или 2.")


def get_coordinates():
    """Получает координаты костяшки от пользователя."""

    while True:
        user_input = input(
            "\nВведите координаты костяшки "
            "(строка столбец, от 1 до 4) "
            "или 'q' для выхода: "
        ).strip()

        if user_input.lower() == "q":
            return None

        parts = user_input.split()

        if len(parts) != 2:
            print("Ошибка: необходимо ввести два числа.")
            continue

        try:
            row = int(parts[0])
            col = int(parts[1])
        except ValueError:
            print("Ошибка: координаты должны быть числами.")
            continue

        if not (1 <= row <= 4 and 1 <= col <= 4):
            print("Ошибка: координаты должны быть от 1 до 4.")
            continue

        return row - 1, col - 1