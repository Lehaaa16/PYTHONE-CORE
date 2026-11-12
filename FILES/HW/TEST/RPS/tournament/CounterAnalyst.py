import random


class CounterAnalyst:
    def __init__(self, name="Контр-Аналітик"):
        self.name = name
        self.opponent_history = []
        self.my_history = []

        self.ram_window_size = 10
        self.opponent_counts = {"камень": 0, "ножницы": 0, "бумага": 0}
        self.consecutive_copies = 0

        self.detected_class = "UNKNOWN"
        self.class_lock_counter = 0

        # Додаткова пам'ять для відстеження динаміки останніх ходів (тренд)
        self.recent_opponent_window = []

    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]

        if len(self.my_history) < self.ram_window_size or len(self.opponent_history) < self.ram_window_size:
            move = random.choice(moves)
            self.my_history.append(move)
            return move

        current_round = len(self.my_history)

        # 🛡️ 1. Детекція дзеркала
        if self.consecutive_copies > 10:
            self.detected_class = "MIRROR"

        # 🔄 2. Розширена класифікація з урахуванням Динаміки (Динамічний Накопичувач vs Упертюх)
        elif current_round % 50 == 0 and self.class_lock_counter == 0:  # Скоротили період перевірки до 50 ходів для гнучкості
            total = len(self.opponent_history)
            dominant = max(self.opponent_counts, key=lambda k: self.opponent_counts[k])
            dom_freq = self.opponent_counts[dominant] / total

            # Перевіряємо, чи тренд мінливий (Динамічний накопичувач змінює ваги)
            recent_trend = self.recent_opponent_window[-20:] if len(
                self.recent_opponent_window) >= 20 else self.recent_opponent_window
            recent_unique_moves = len(set(recent_trend))

            if dom_freq > 0.45 and recent_unique_moves <= 2:
                self.detected_class = "MONOPOLIST"  # Жорсткий упертюх (як Камінь)
            elif dom_freq > 0.35:
                self.detected_class = "DYNAMIC_ACCUM"  # Динамічний накопичувач (плавний зсув ваг)
            else:
                self.detected_class = "ANALYST"  # Майстер-Аналітик

            self.class_lock_counter = 25  # Зменшили блокування до 25 ходів, щоб бот встигав адаптуватися до динаміки!

        if self.class_lock_counter > 0:
            self.class_lock_counter -= 1

        counter_map = {
            "камень": "бумага",
            "ножницы": "камень",
            "бумага": "ножницы"
        }

        # 🎯 3. ВИБІР ТАКТИКИ ЗАЛЕЖНО ВІД РОЗШИРЕНОГО КЛАСУ
        if self.detected_class == "MIRROR":
            smart_move = random.choice(moves)

        elif self.detected_class == "MONOPOLIST":
            # Б'ємо прямим контр-ходом упертюха
            dominant_opponent_move = max(self.opponent_counts, key=lambda k: self.opponent_counts[k])
            smart_move = counter_map[dominant_opponent_move]

        elif self.detected_class == "DYNAMIC_ACCUMULATION" or self.detected_class == "DYNAMIC_ACCUM":
            # Проти Динамічного Накопичувача: дивимося виключно на його коротке вікно (останні 10 ходів),
            # щоб не залежати від застарілої глобальної статистики, яку він сам же й змінює!
            recent_accum_moves = self.opponent_history[-10:]
            acc_counts = {m: recent_accum_moves.count(m) for m in moves}
            acc_favorite = max(acc_counts, key=lambda k: acc_counts[k])
            smart_move = counter_map[acc_favorite]

        else:
            # Логіка другого порядку проти Майстра-Аналітика
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
        self.recent_opponent_window.append(opponent_move)

        if opponent_move in self.opponent_counts:
            self.opponent_counts[opponent_move] += 1

        if len(self.my_history) > 1 and opponent_move == self.my_history[-2]:
            self.consecutive_copies += 1
        else:
            self.consecutive_copies = max(0, self.consecutive_copies - 1)