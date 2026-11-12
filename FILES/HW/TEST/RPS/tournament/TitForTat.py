import random

class TitForTat:
    def __init__(self, name="Наслідувач"):
        self.name = name
        self.last_opponent_move = None
        self.choices = ["камень", "ножницы", "бумага"]

    def make_move(self):
        if self.last_opponent_move is None:
            return random.choice(self.choices)
        return self.last_opponent_move

    def observe(self, opponent_move):
        self.last_opponent_move = opponent_move