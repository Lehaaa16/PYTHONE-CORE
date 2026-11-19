import random

# Возможные ходы
choices = ["камень", "ножницы", "бумага"]


def get_human_move(last_move, last_result):
    """Симулирует ход человека с учетом психологических паттернов."""
    if last_move is None:
        # В самом начале люди чаще выбирают камень
        return random.choices(choices, weights=[0.5, 0.25, 0.25], k=1)[0]

    if last_result == "win":
        # Победив, человек склонен повторить знак (Win-Stay)
        weights_map = {
            "камень": [0.6, 0.2, 0.2],
            "ножницы": [0.2, 0.6, 0.2],
            "бумага": [0.2, 0.2, 0.6]
        }
    elif last_result == "loss":
        # Проиграв, человек старается сменить знак (Lose-Shift)
        weights_map = {
            "камень": [0.1, 0.45, 0.45],
            "ножницы": [0.45, 0.1, 0.45],
            "бумага": [0.45, 0.45, 0.1]
        }
    else:
        # При ничьей выбор более равномерный
        weights_map = {
            "камень": [0.33, 0.33, 0.34],
            "ножницы": [0.34, 0.33, 0.33],
            "бумага": [0.33, 0.34, 0.33]
        }

    return random.choices(choices, weights=weights_map[last_move], k=1)[0]


def get_robot_move():
    """Робот использует чистый рандомайзер."""
    return random.choice(choices)


def determine_winner(human, robot):
    """Определяет победителя раунда."""
    if human == robot:
        return "draw"
    elif (human == "камень" and robot == "ножницы") or \
            (human == "ножницы" and robot == "бумага") or \
            (human == "бумага" and robot == "камень"):
        return "human"
    else:
        return "robot"


# Инициализация счетчиков
total_games = 1000000

human_stats = {"камень": 0, "ножницы": 0, "бумага": 0}
robot_stats = {"камень": 0, "ножницы": 0, "бумага": 0}

human_wins = 0
robot_wins = 0
draws = 0

last_human_move = None
last_human_result = "draw"

# Основной цикл симуляции
for _ in range(total_games):
    # Делают ходы
    h_move = get_human_move(last_human_move, last_human_result)
    r_move = get_robot_move()

    # Считаем статистику ходов
    human_stats[h_move] += 1
    robot_stats[r_move] += 1

    # Определяем результат раунда для человека
    result = determine_winner(h_move, r_move)
    if result == "human":
        human_wins += 1
        last_human_result = "win"
    elif result == "robot":
        robot_wins += 1
        last_human_result = "loss"
    else:
        draws += 1
        last_human_result = "draw"

    last_human_move = h_move

# Вывод результатов
print("=" * 40)
print(f"КУДА ЖЕ БЕЗ СТАТИСТИКИ? (Всего игр: {total_games})")
print("=" * 40)

print("\n👤 СТАТИСТИКА ЧЕЛОВЕКА:")
for move, count in human_stats.items():
    percent = (count / total_games) * 100
    print(f"  - {move.capitalize()}: {count} раз ({percent:.2f}%)")

print("\n🤖 СТАТИСТИКА РОБОТА:")
for move, count in robot_stats.items():
    percent = (count / total_games) * 100
    print(f"  - {move.capitalize()}: {count} раз ({percent:.2f}%)")

print("\n🏆 ИТОГИ МАТЧА:")
print(f"  - Побед человека: {human_wins} ({(human_wins / total_games) * 100:.2f}%)")
print(f"  - Побед робота: {robot_wins} ({(robot_wins / total_games) * 100:.2f}%)")
print(f"  - Ничьих: {draws} ({(draws / total_games) * 100:.2f}%)")

print("\n" + "=" * 40)
if human_wins > robot_wins:
    print("🏆 В ИТОГЕ ВЫИГРАЛ: ЧЕЛОВЕК (за счет перекоса вероятностей)")
elif robot_wins > human_wins:
    print("🏆 В ИТОГЕ ВЫИГРАЛ: РОБОТ")
else:
    print("🤝 НИЧЬЯ!")
print("=" * 40)