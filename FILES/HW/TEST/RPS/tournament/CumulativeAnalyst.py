import random


class CumulativeAnalyst:
    def __init__(self, name="Динамічний Накопичувач"):
        self.name = name
        self.opponent_history = []
        # Одразу зберігаємо лічильники, щоб не перераховувати всю історію щоразу!
        self.counts = {"камінь": 0, "ножиці": 0, "папір": 0}

    def make_move(self):
        moves = ["камінь", "ножиці", "папір"]

        # Якщо історії ще немає, ходимо випадково
        if not self.opponent_history:
            return random.choice(moves)

        # Знаходимо найчастіший хід за допомогою готового словника (миттєво!)
        most_frequent = max(self.counts, key=lambda k: self.counts[k])

        # Визначаємо ідеальний контр-хід проти улюбленого знака суперника
        counter_map = {
            "камінь": "папір",  # папір б'є камінь
            "ножиці": "камінь",  # камінь б'є ножиці
            "папір": "ножиці"  # ножиці б'ють папір
        }
        optimal_counter = counter_map[most_frequent]

        # Прогресивне накопичення: починаємо з 33% і додаємо +1% за кожен раунд (максимум до 80%)
        rounds_played = len(self.opponent_history)
        counter_prob = min(0.33 + rounds_played * 0.01, 0.80)

        other_moves = [m for m in moves if m != optimal_counter]
        remaining_prob = 1.0 - counter_prob

        other_prob = remaining_prob / len(other_moves)

        # Формуємо ймовірності для вибору руху
        weights = [counter_prob if m == optimal_counter else other_prob for m in moves]
        return random.choices(moves, weights=weights, k=1)[0]

    def observe(self, opponent_move):
        self.opponent_history.append(opponent_move)
        # Оновлюємо лічильник прямо під час спостереження за 1 крок O(1), замість перебору всієї історії!
        if opponent_move in self.counts:
            self.counts[opponent_move] += 1