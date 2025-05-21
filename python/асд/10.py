import random


def simulate_egg_drop():
    N = random.randint(1, 100)
    eggs = 2
    attempts = 0
    step = 14  # X + (X – 1) + (X – 2) + … + 1 = 100 -> X = 14 .книга Гейла Макдауэлла.
    current_floor = step  # Текущий этаж

    print(f"этаж: {N}")

    while eggs > 0 and current_floor <= 100:
        attempts += 1
        print(f"Попытка {attempts}: Бросаем яйцо с {current_floor}-го этажа.", end=" ")

        if current_floor >= N:
            eggs -= 1
            print("Яйцо разбилось!")
            print(f"Осталось яиц: {eggs}")

            if eggs == 1:
                lower_bound = current_floor - step + 1 if attempts > 1 else 1
                print(f"Начинаем линейный поиск между {lower_bound} и {current_floor - 1}...")

                for floor in range(lower_bound, current_floor):
                    attempts += 1
                    print(f"Попытка {attempts}: Бросаем яйцо с {floor}-го этажа.", end=" ")

                    if floor >= N:
                        eggs -= 1
                        print("Яйцо разбилось!")
                        print(f"Найден критический этаж N = {floor}!")
                        return floor, attempts
                    else:
                        print("Яйцо не разбилось.")
                print(f"Найден критический этаж N = {current_floor - 1}!")
                return current_floor - 1, attempts

        else:
            print("Яйцо не разбилось.")

        step -= 1
        current_floor += step

    if eggs == 0 and current_floor < N:
        print("Не удалось найти N (яйца закончились)!")
        return -1, attempts
    else:
        print(f"Найден критический этаж N = 100!")
        return 100, attempts


N, attempts = simulate_egg_drop()
print(f"\nРезультат: Нужный этаж N = {N}, найдено за {attempts} попыток.")