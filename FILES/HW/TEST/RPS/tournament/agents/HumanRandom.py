import random


class HumanRandom:
    def __init__(self, name="Звичайна людина"):
        self.name = name
        self.choices = ["камінь", "ножиці", "папір"]
        self.last_move = None
        self.last_result = "draw"

    def make_move(self):
        if self.last_move is None:
            return random.choices(self.choices, weights=[0.4, 0.3, 0.3], k=1)[0]

        # Елементи людської психології (Win-stay / lose-shift)
        if self.last_result == "win":
            weights_map = {
                "камінь": [0.5, 0.25, 0.25],
                "ножиці": [0.25, 0.5, 0.25],
                "папір": [0.25, 0.25, 0.5]
            }
            weights = weights_map.get(self.last_move, [0.33, 0.33, 0.34])
        elif self.last_result == "loss":
            weights_map = {
                "камінь": [0.2, 0.4, 0.4],
                "ножиці": [0.4, 0.2, 0.4],
                "папір": [0.4, 0.4, 0.2]
            }
            weights = weights_map.get(self.last_move, [0.33, 0.33, 0.34])
        else:
            weights = [0.33, 0.33, 0.34]

        self.last_move = random.choices(self.choices, weights=weights, k=1)[0]
        return self.last_move

    def observe(self, opponent_move):
        pass