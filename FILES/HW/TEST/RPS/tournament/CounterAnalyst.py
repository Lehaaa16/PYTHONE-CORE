import random


class SmartMetaBot:
    def __init__(self, name="Мета-Лис"):
        self.name = name
        self.opponent_history = []
        self.my_history = []

    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]

        # На початку граємо випадково, збираємо мінімум даних
        if len(self.my_history) < 5:
            move = random.choice(moves)
            self.my_history.append(move)
            return move

        # Емуляція логіки аналітика: дивимося, що наш суперник міг подумати про наші останні ходи
        recent_mine = self.my_history[-5:]
        counts = {m: recent_mine.count(m) for m in moves}

        # Використовуємо лямбду замість .get(), щоб прибрати попередження PyCharm
        my_favorite = max(counts, key=lambda k: counts[k])

        # Аналітик на основі нашого улюбленого ходу вибере свій контр-хід:
        counter_map = {
            "камень": "бумага",
            "ножницы": "камень",
            "бумага": "ножницы"
        }
        analyst_expected_move = counter_map[my_favorite]

        # А тепер МИ робимо контр-хід на очікування аналітика! (б'ємо його майбутній удар)
        reverse_counter_map = {
            "бумага": "ножницы",
            "камень": "бумага",
            "ножницы": "камень"
        }
        smart_move = reverse_counter_map[analyst_expected_move]

        # Зберігаємо свій хід і повертаємо його
        self.my_history.append(smart_move)
        return smart_move

    def observe(self, opponent_move):
        self.opponent_history.append(opponent_move)
