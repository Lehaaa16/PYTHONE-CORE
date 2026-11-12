import random


class CounterAnalyst:
    def __init__(self, name="Контр-Аналітик"):
        self.name = name
        self.opponent_history = []
        self.my_history = []

        self.ram_window_size = 10
        self.opponent_counts = {"камень": 0, "ножницы": 0, "бумага": 0}
        self.consecutive_copies = 0

        # Поточний визначений «клас» суперника (за замовчуванням: невідомо)
        self.detected_class = "UNKNOWN"
        self.class_lock_counter = 0  # Захист від частих перемикань ("тактика по зміні тактики")

    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]

        if len(self.my_history) < self.ram_window_size or len(self.opponent_history) < self.ram_window_size:
            move = random.choice(moves)
            self.my_history.append(move)
            return move

        current_round = len(self.my_history)

        # 🛡️ 1. Детекція класу "Дзеркало" (Наслідувач)
        if self.consecutive_copies > 12:
            self.detected_class = "MIRROR"

        # 🔄 2. Регулярна перевдка класів (щоб уникнути зайвих стрибків, робимо це раз на 100 раундів)
        elif current_round % 100 == 0 and self.class_lock_counter == 0:
            total = len(self.opponent_history)
            dominant = max(self.opponent_counts, key=lambda k: self.opponent_counts[k])
            dom_freq = self.opponent_counts[dominant] / total

            if dom_freq > 0.40:
                self.detected_class = "MONOPOLIST"  # (Упертюх або Накопичувач)
            else:
                self.detected_class = "ANALYST"  # (Майстер-Аналітик та інші)

            self.class_lock_counter = 50  # Заморожуємо вибір класу на 50 раундів (стабілізація)

        if self.class_lock_counter > 0:
            self.class_lock_counter -= 1

        counter_map = {
            "камень": "бумага",
            "ножницы": "камень",
            "бумага": "ножницы"
        }

        # 🎯 3. ВИБІР ТАКТИКИ ЗАЛЕЖНО ВІД КЛАСУ СУПЕРНИКА
        if self.detected_class == "MIRROR":
            # Тактика проти Наслідувача: ламаємо дзеркало хаосом
            smart_move = random.choice(moves)

        elif self.detected_class == "MONOPOLIST":
            # Тактика проти Упертюха / Накопичувача: б'ємо прямим контр-ходом
            dominant_opponent_move = max(self.opponent_counts, key=lambda k: self.opponent_counts[k])
            smart_move = counter_map[dominant_opponent_move]

        else:
            # Тактика за замовчуванням проти Аналітиків (Майстер-Аналітик): Теорія другого порядку
            recent_mine = self.my_history[-self.ram_window_size:]
            counts = {m: recent_mine.count(m) for m in moves}
            my_favorite = max(counts, key=lambda k: counts[k])

            analyst_expected_move = counter_map[my_favorite]

            reverse_counter_map = {
                "бумага": "ножницы",
                "камень": "бумага",
                "ножницы": "камень"
            }
            smart_move = reverse_counter_map[analyst_expected_move]

        self.my_history.append(smart_move)
        return smart_move

    def observe(self, opponent_move):
        self.opponent_history.append(opponent_move)

        if opponent_move in self.opponent_counts:
            self.opponent_counts[opponent_move] += 1

        # Оновлення лічильника дзеркала в реальному часі O(1)
        if len(self.my_history) > 1 and opponent_move == self.my_history[-2]:
            self.consecutive_copies += 1
        else:
            self.consecutive_copies = max(0, self.consecutive_copies - 1)