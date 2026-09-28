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


def get_tile():
    """Получает номер костяшки от пользователя."""

    while True:
        user_input = input(
            "\nВведите номер костяшки (1-15) "
            "или 'q' для выхода: "
        ).strip()

        if user_input.lower() == "q":
            return None

        try:
            tile = int(user_input)
        except ValueError:
            print("Ошибка: необходимо ввести число от 1 до 15.")
            continue

        if not 1 <= tile <= 15:
            print("Ошибка: номер костяшки должен быть от 1 до 15.")
            continue

        return tile