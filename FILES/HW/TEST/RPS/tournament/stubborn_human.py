import random

class StubbornHuman:
    def __init__(self, name="Упрямец (Камень)", weights=(0.6, 0.2, 0.2)):
        self.name = name
        self.weights = weights  # камень, ножницы, бумага
        self.choices = ["камень", "ножницы", "бумага"]

    def make_move(self):
        return random.choices(self.choices, weights=self.weights, k=1)[0]

    def observe(self, opponent_move):
        pass  # Упрямец не учится на ошибках