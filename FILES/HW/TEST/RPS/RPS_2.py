import random

choices = ["камень", "ножницы", "бумага"]


def get_counter_move(move):
    """Возвращает ход, который побеждает переданный жест."""
    if move == "камень":
        return "бумага"
    elif move == "ножницы":
        return "камень"
    else:
        return "ножницы"


# 1. Мастер-Аналитик (анализирует последние 10 ходов и плавно меняет веса)
class SlidingAnalyst:
    def __init__(self, name, window_size=10):
        self.name = name
        self.window_size = window_size
        self.opponent_history = []

    def make_move(self):
        if len(self.opponent_history) < 3:
            # Сначала играем случайно
            return random.choice(choices)

        # Берем только последние N ходов (скользящее окно)
        recent = self.opponent_history[-self.window_size:]
        total = len(recent)

        # Считаем частоту ходов в окне
        p_rock = recent.count("камень") / total
        p_scissors = recent.count("ножницы") / total
        p_paper = recent.count("бумага") / total

        # Вычисляем веса для НАШИХ ответов (чтобы побить их частые ходы)
        # Если он часто бьет камень (p_rock), мы повышаем вес бумаги
        w_rock = 0.2 + 0.6 * p_scissors
#        сильнее
#        бьем
#        ножницы
        w_scissors = 0.2 + 0.6 * p_paper
#        сильнее
#        бьем
#        бумагу
        w_paper = 0.2 + 0.6 * p_rock
#        сильнее
#        бьем
#        камень

        weights = [w_rock, w_scissors, w_paper]
        return random.choices(choices, weights=weights, k=1)[0]

    def observe(self, opponent_move):
        self.opponent_history.append(opponent_move)


# 2. Игрок «Око за око» (Tit-for-Tat / Подражатель)
class TitForTat:
    def __init__(self, name):
        self.name = name
        self.last_opponent_move = None

    def make_move(self):
        if self.last_opponent_move is None:
            # Первый ход — случайный
            return random.choice(choices)
        # Копируем то, что соперник сделал в прошлый раз
        return self.last_opponent_move

    def observe(self, opponent_move):
        self.last_opponent_move = opponent_move


# --- ЗАПУСК СИМУЛЯЦИИ НА 10 000 ИГР ---
total_games = 10000

analyst = SlidingAnalyst("Мастер-Аналитик (окно 10)")
copycat = TitForTat("Игрок 'Око за око'")

# Статистика ходов
stats_analyst = {"камень": 0, "ножницы": 0, "бумага": 0}
stats_copycat = {"камень": 0, "ножницы": 0, "бумага": 0}

wins_analyst = 0
wins_copycat = 0
draws = 0

# Первый ход для инициализации
move_a = analyst.make_move()
move_c = copycat.make_move()

for _ in range(total_games):
    # Фиксируем ходы
    stats_analyst[move_a] += 1
    stats_copycat[move_c] += 1

    # Перекрестное наблюдение
    analyst.observe(move_c)
    copycat.observe(move_a)

    # Определяем победителя раунда
    if move_a == move_c:
        draws += 1
    elif (move_a == "камень" and move_c == "ножницы") or \
            (move_a == "ножницы" and move_c == "бумага") or \
            (move_a == "бумага" and move_c == "камень"):
        wins_analyst += 1
    else:
        wins_copycat += 1

    # Готовим ходы на следующий раунд
    move_a = analyst.make_move()
    move_c = copycat.make_move()

# --- ВЫВОД РЕЗУЛЬТАТОВ ---
print("=" * 55)
print(f" ТУРНИР СТРАТЕГИЙ (Игр: {total_games})")
print("=" * 55)

print(f"\n📈 СТАТИСТИКА '{analyst.name}':")
for move, count in stats_analyst.items():
    print(f"  - {move.capitalize()}: {count} раз ({(count / total_games) * 100:.2f}%)")

print(f"\n🪞 СТАТИСТИКА '{copycat.name}':")
for move, count in stats_copycat.items():
    print(f"  - {move.capitalize()}: {count} раз ({(count / total_games) * 100:.2f}%)")

print("\n🏆 СЧЕТ МАТЧА:")
print(f"  - Побед Аналитика: {wins_analyst} ({(wins_analyst / total_games) * 100:.2f}%)")
print(f"  - Побед Подражателя: {wins_copycat} ({(wins_copycat / total_games) * 100:.2f}%)")
print(f"  - Ничьих: {draws} ({(draws / total_games) * 100:.2f}%)")

print("\n" + "=" * 55)
if wins_analyst > wins_copycat:
    print(f"🏆 ПОБЕДИТЕЛЬ: {analyst.name}")
elif wins_copycat > wins_analyst:
    print(f"🏆 ПОБЕДИТЕЛЬ: {copycat.name}")
else:
    print("🤝 НИЧЬЯ!")
print("=" * 55)