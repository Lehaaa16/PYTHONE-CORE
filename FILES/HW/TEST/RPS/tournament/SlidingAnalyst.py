import random


class SlidingAnalyst:
    def __init__(self, name="Мастер-Аналитик", window_size=10):
        self.name = name
        self.window_size = window_size
        self.opponent_history = []
        self.choices = ["камень", "ножницы", "бумага"]

    def make_move(self):
        if len(self.opponent_history) < 3:
            return random.choice(self.choices)

        recent = self.opponent_history[-self.window_size:]
        total = len(recent)

        p_rock = recent.count("камень") / total
        p_scissors = recent.count("ножницы") / total
        p_paper = recent.count("бумага") / total

        # Веса для наших ответов (бьем частые ходы противника)
        w_rock = 0.2 + 0.6 * p_scissors  # бьем ножницы
        w_scissors = 0.2 + 0.6 * p_paper  # бьем бумагу
        w_paper = 0.2 + 0.6 * p_rock  # бьем камень

        return random.choices(self.choices, weights=[w_rock, w_scissors, w_paper], k=1)[0]

    def observe(self, opponent_move):
        self.opponent_history.append(opponent_move)