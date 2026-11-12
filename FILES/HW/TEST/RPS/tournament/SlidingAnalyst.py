import random


class SlidingAnalyst:
    def __init__(self, name="Майстер-Аналітик", window_size=10):
        self.name = name
        self.window_size = window_size
        self.opponent_history = []
        self.choices = ["камінь", "ножиці", "папір"]

    def make_move(self):
        if len(self.opponent_history) < 3:
            return random.choice(self.choices)

        recent = self.opponent_history[-self.window_size:]
        total = len(recent)

        p_rock = recent.count("камінь") / total
        p_scissors = recent.count("ножиці") / total
        p_paper = recent.count("папір") / total

        # Ваги для наших відповідей (б'ємо часті ходи противника)
        w_rock = 0.2 + 0.6 * p_scissors  # б'ємо ножиці
        w_scissors = 0.2 + 0.6 * p_paper  # б'ємо папір
        w_paper = 0.2 + 0.6 * p_rock  # б'ємо камінь

        return random.choices(self.choices, weights=[w_rock, w_scissors, w_paper], k=1)[0]

    def observe(self, opponent_move):
        self.opponent_history.append(opponent_move)