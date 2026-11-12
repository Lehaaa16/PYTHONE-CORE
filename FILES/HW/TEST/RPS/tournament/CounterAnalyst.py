import random


class CounterAnalyst:
    def __init__(self, name="Контр-Аналітик"):
        self.name = name
        self.opponent_history = []
        self.my_history = []

        # 💾 ЖОРСТКИЙ ДИСК (Глобальна пам'ять)
        self.global_opponent_counts = {"камень": 0, "ножницы": 0, "бумага": 0}

        # ⚡ ОПЕРАТИВНА ПАМ'ЯТЬ (Вікно 10, синхронізоване з Майстром)
        self.ram_window_size = 10

        self.sync_interval = 500
        self.long_term_weight = 0.15
        self.hybrid_scores = {"камень": 1.0, "ножницы": 1.0, "бумага": 1.0}

        # O(1) оптимізація для детектора Наслідувача (без повільних циклів)
        self.consecutive_copies = 0

    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]

        if len(self.my_history) < self.ram_window_size or len(self.opponent_history) < self.ram_window_size:
            move = random.choice(moves)
            self.my_history.append(move)
            return move

        current_round = len(self.my_history)

        # 🛡️ ШВИДКИЙ ДЕТЕКТОР НАСЛІДУВАЧА O(1)
        # Якщо опонент занадто часто копіює наш попередній хід, вносимо хаос, щоб уникнути нічиїх
        if self.consecutive_copies > 15:
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

        # 1. Опитування оперативки (вікно 10)
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

        # O(1) оновлення лічильника наслідування на льоту
        if len(self.my_history) > 1 and opponent_move == self.my_history[-2]:
            self.consecutive_copies += 1
        else:
            self.consecutive_copies = max(0, self.consecutive_copies - 1)