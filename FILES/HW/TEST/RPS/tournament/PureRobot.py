import random

class PureRobot:
    def __init__(self, name="Робот-Рандомайзер"):
        self.name = name
        self.choices = ["камень", "ножницы", "бумага"]

    def make_move(self):
        return random.choice(self.choices)

    def observe(self, opponent_move):
        pass