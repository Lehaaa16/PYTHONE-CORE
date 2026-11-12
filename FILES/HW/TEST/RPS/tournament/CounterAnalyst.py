import random


class CounterAnalyst:
    def __init__(self, name="Контр-Аналітик"):
        self.name = name
        self.opponent_history = []
        self.my_history = []

        # 💾 ЖОРСТКИЙ ДИСК (Глобальна пам'ять)
        self.global_opponent_counts = {"камень": 0, "ножницы": 0, "бумага": 0}

        # ⚡ ОПЕРАТИВНА ПАМ'ЯТЬ: Збільшуємо до 10, щоб збігатися з вікном Майстра-Аналітика!
        self.ram_window_size = 10

        self.sync_interval = 500
        self.long_term_weight = 0.15
        self.hybrid_scores = {"камень": 1.0, "ножницы": 1.0, "бумага": 1.0}

    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]

        # На початку збираємо базу
        if len(self.my_history) < self.ram_window_size or len(self.opponent_history) < self.ram_window_size:
            move = random.choice(moves)
            self.my_history.append(move)
            return move

        current_round = len(self.my_history)

        # 🛡️ ДЕТЕКТОР НАСЛІДУВАЧА (Anti-Tit-for-Tat)
        # Якщо опонент у більшості випадків просто копіює наш попередній хід — руйнуємо петлю!
        if len(self.opponent_history) >= 10:
            copies_count = sum(1 for i in range(1, len(self.opponent_history))
                               if self.opponent_history[i] == self.my_history[i - 1])
            if (copies_count / len(self.opponent_history)) > 0.7:
                # Опонент — Наслідувач! Робимо випадковий зсув, щоб розірвати нічиї
                anti_mirror_move = random.choice(moves)
                self.my_history.append(anti_mirror_move)
                return anti_mirror_move

        # 🔄 СИНХРОНІЗАЦІЯ ПАМ'ЯТІ (HDD + RAM)
        if current_round % self.sync_interval == 0:
            total_global = sum(self.global_opponent_counts.values())
            if total_global > 0:
                for m in moves:
                    global_freq = self.global_opponent_counts[m] / total_global
                    self.hybrid_scores[m] = (1.0 - self.long_term_weight) * self.hybrid_scores[m] + \
                                            self.long_term_weight * (global_freq * 3.0)

        # 1. Опитування оперативки (тепер вікно рівно 10, як у Майстра)
        recent_mine = self.my_history[-self.ram_window_size:]
        local_counts = {m: recent_mine.count(m) for m in moves}

        combined_evaluation = {}
        for m in moves:
            combined_evaluation[m] = local_counts.get(m, 0) + self.hybrid_scores.get(m, 1.0)

        my_favorite = max(combined_evaluation, key=lambda k: combined_evaluation[k])

        # 2. Логіка випередження Майстра-Аналітика
        counter_map = {
            "камень": "бумага",
            "ножницы": "камень",
            "бумага": "ножницы"
        }
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
        if opponent_move in self.global_opponent_counts:
            self.global_opponent_counts[opponent_move] += 1