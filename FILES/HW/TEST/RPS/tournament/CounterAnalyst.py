import random


class CounterAnalyst:
    def __init__(self, name="Контр-Аналітик"):
        self.name = name
        self.opponent_history = []
        self.my_history = []

        # 💾 ЖОРСТКИЙ ДИСК (Глобальна пам'ять на всю довгу дистанцію)
        self.global_opponent_counts = {"камень": 0, "ножницы": 0, "бумага": 0}

        # ⚡ ОПЕРАТИВНА ПАМ'ЯТЬ (Коротке вікно для швидких тактичних рішень)
        self.ram_window_size = 5

        # Зважені коефіцієнти для змішування (пам'ять HDD і оперативки RAM)
        self.sync_interval = 500  # Кожні 500 ходів робимо синхронізацію
        self.long_term_weight = 0.15  # М'який вплив жорсткого диска (15%), щоб не зіпсувати тактику

        # Кориговані бали для ходів (гібридна пам'ять)
        self.hybrid_scores = {"камень": 1.0, "ножницы": 1.0, "бумага": 1.0}

    def make_move(self):
        moves = ["камень", "ножницы", "бумага"]

        # На початку збираємо мінімальну базу
        if len(self.my_history) < self.ram_window_size:
            move = random.choice(moves)
            self.my_history.append(move)
            return move

        current_round = len(self.my_history)

        # 🔄 СИНХРОНІЗАЦІЯ ПАМ'ЯТІ (Магія злиття HDD та RAM)
        # Кожні N ходів ми дивимося на "жорсткий диск" і злегка оновлюємо гібридні бали
        if current_round % self.sync_interval == 0:
            total_global = sum(self.global_opponent_counts.values())
            if total_global > 0:
                for m in moves:
                    # Частота цього ходу на глобальному диску
                    global_freq = self.global_opponent_counts[m] / total_global
                    # Плавне коригування гібридного бала з урахуванням ваги жорсткого диска
                    self.hybrid_scores[m] = (1.0 - self.long_term_weight) * self.hybrid_scores[m] + \
                                            self.long_term_weight * (global_freq * 3.0)

        # 1. Беремо оперативку (останні ходи) для визначення того, що робить опонент прямо зараз
        recent_mine = self.my_history[-self.ram_window_size:]
        local_counts = {m: recent_mine.count(m) for m in moves}

        # Комбінуємо оперативну частоту з гібридними балами з жорсткого диска
        combined_evaluation = {}
        for m in moves:
            # Локальна вага + бонус з довгової пам'яті (гібридний підхід)
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

        # Паралельно пишемо все на "жорсткий диск" O(1)
        if opponent_move in self.global_opponent_counts:
            self.global_opponent_counts[opponent_move] += 1