from SlidingAnalyst import SlidingAnalyst
from TitForTat import TitForTat
from Stubborn_human import StubbornHuman
from HumanRandom import HumanRandom
from PureRobot import PureRobot


# ANSI-коды для красивого цветного вывода в консоли
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def determine_winner(m1, m2):
    if m1 == m2:
        return "draw"
    elif (m1 == "камень" and m2 == "ножницы") or \
            (m1 == "ножницы" and m2 == "бумага") or \
            (m1 == "бумага" and m2 == "камень"):
        return "p1"
    else:
        return "p2"


def play_match(player1, player2, games_count):
    p1_wins = 0
    p2_wins = 0
    local_draws = 0

    # Сброс состояния перед матчем
    for p in (player1, player2):
        if hasattr(p, 'opponent_history'): p.opponent_history = []
        if hasattr(p, 'last_opponent_move'): p.last_opponent_move = None
        if hasattr(p, 'last_move'): p.last_move = None
        if hasattr(p, 'last_result'): p.last_result = "draw"

    m1 = player1.make_move()
    m2 = player2.make_move()

    for _ in range(games_count):
        res = determine_winner(m1, m2)
        if res == "p1":
            p1_wins += 1
            if hasattr(player1, 'last_result'): player1.last_result = "win"
            if hasattr(player2, 'last_result'): player2.last_result = "loss"
        elif res == "p2":
            p2_wins += 1
            if hasattr(player1, 'last_result'): player1.last_result = "loss"
            if hasattr(player2, 'last_result'): player2.last_result = "win"
        else:
            local_draws += 1
            if hasattr(player1, 'last_result'): player1.last_result = "draw"
            if hasattr(player2, 'last_result'): player2.last_result = "draw"

        player1.observe(m2)
        player2.observe(m1)

        m1 = player1.make_move()
        m2 = player2.make_move()

    return p1_wins, p2_wins, local_draws


# --- ИНТЕРАКТИВНЫЙ ВВОД КОЛИЧЕСТВА ИГР ---
print(f"{Colors.YELLOW}{Colors.BOLD}=== НАСТРОЙКА ТУРНИРА ПО КАМЕНЬ-НОЖНИЦЫ-БУМАГА ==={Colors.RESET}")
print(f"{Colors.GREEN}В турнире участвуют 5 ботов. Всего будет сыграно 10 парных дуэлей.{Colors.RESET}")
user_input = input(f"{Colors.BLUE}Введите количество матчей для одной дуэли: {Colors.RESET}")

try:
    games_per_duel = int(user_input)
except ValueError:
    games_per_duel = 1000
    print(f"{Colors.RED}Введено не число! Автоматически установлено значение по умолчанию: 1000.{Colors.RESET}")

total_all_games = games_per_duel * 10
print(f"\n{Colors.RED}{Colors.BOLD}⚠️ ВНИМАНИЕ: Так как участников 5, всего пройдет 10 парных дуэлей.")
print(
    f"Общее количество сыгранных раундов во всем турнире составит: {total_all_games} ({games_per_duel} × 10){Colors.RESET}\n")

input(f"{Colors.HEADER}{Colors.BOLD}Нажмите Enter, чтобы запустить турнир...{Colors.RESET}")

# Описание участников
print(f"\n{Colors.HEADER}{Colors.BOLD}" + "=" * 65)
print(" 🤖 УЧАСТНИКИ ТУРНИРА И ИХ СТРАТЕГИИ:")
print("=" * 65 + f"{Colors.RESET}")
print(
    f"1. {Colors.BOLD}Мастер-Аналитик{Colors.RESET}: Анализирует последние 10 ходов соперника и плавно подстраивает веса.")
print(
    f"2. {Colors.BOLD}Подражатель{Colors.RESET}: Реализует тактику 'Око за око' (Tit-for-Tat) — копирует прошлый ход противника.")
print(f"3. {Colors.BOLD}Упрямец (Камень){Colors.RESET}: Человек с перекосом характера, обожающий кидать камень (60%).")
print(f"4. {Colors.BOLD}Обычный человек{Colors.RESET}: Симулирует человеческую психологию (Win-Stay / Lose-Shift).")
print(f"5. {Colors.BOLD}Робот-Рандомайзер{Colors.RESET}: Классический чистый рандом (33%/33%/33%).\n")

# Список всех участников
players_classes = [
    lambda: SlidingAnalyst("Мастер-Аналитик"),
    lambda: TitForTat("Подражатель"),
    lambda: StubbornHuman("Упрямец (Камень)"),
    lambda: HumanRandom("Обычный человек"),
    lambda: PureRobot("Робот-Рандомайзер")
]

# Статистика: победы в матчах и общие очки (выигранные раунды/ничьи/проигрыши)
match_scores = {cls().name: 0 for cls in players_classes}
total_rounds_stats = {cls().name: {"wins": 0, "losses": 0, "draws": 0} for cls in players_classes}

print(f"{Colors.HEADER}{Colors.BOLD}" + "=" * 65)
print(" 🏆 НАЧАЛО КРУГОВОГО ТУРНИРА 🏆")
print("=" * 65 + f"{Colors.RESET}\n")

n = len(players_classes)

# Круговой турнир
for i in range(n):
    for j in range(i + 1, n):
        p1 = players_classes[i]()
        p2 = players_classes[j]()

        w1, w2, match_draws = play_match(p1, p2, games_per_duel)

        # Собираем статистику раундов
        total_rounds_stats[p1.name]["wins"] += w1
        total_rounds_stats[p1.name]["losses"] += w2
        total_rounds_stats[p1.name]["draws"] += match_draws

        total_rounds_stats[p2.name]["wins"] += w2
        total_rounds_stats[p2.name]["losses"] += w1
        total_rounds_stats[p2.name]["draws"] += match_draws

        print(
            f"{Colors.CYAN}⚔️ Дуэль:{Colors.RESET} {Colors.BOLD}{p1.name}{Colors.RESET} vs {Colors.BOLD}{p2.name}{Colors.RESET}")

        if w1 > w2:
            p1_str = f"{Colors.GREEN}{p1.name}: {w1}{Colors.RESET}"
            p2_str = f"{Colors.RED}{p2.name}: {w2}{Colors.RESET}"
            match_scores[p1.name] += 1
        elif w2 > w1:
            p1_str = f"{Colors.RED}{p1.name}: {w1}{Colors.RESET}"
            p2_str = f"{Colors.GREEN}{p2.name}: {w2}{Colors.RESET}"
            match_scores[p2.name] += 1
        else:
            p1_str = f"{p1.name}: {w1}"
            p2_str = f"{p2.name}: {w2}"

        draws_str = f"Ничьих: {Colors.YELLOW}{match_draws}{Colors.RESET}"

        print(f"   Результат -> {p1_str} | {p2_str} | {draws_str}\n")

print(f"{Colors.YELLOW}{Colors.BOLD}" + "=" * 65)
print(" 👑 ИТОГОВАЯ ТАБЛИЦА ЛИДЕРОВ ТУРНИРА:")
print("=" * 65 + f"{Colors.RESET}")

# Сортируем сначала по выигранным матчам, а при равенстве — по сумме побед в раундах
sorted_leaderboard = sorted(
    match_scores.items(),
    key=lambda item: (item[1], total_rounds_stats[item[0]]["wins"]),
    reverse=True
)

medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

for rank, ((name, match_wins), medal) in enumerate(zip(sorted_leaderboard, medals), 1):
    r_stats = total_rounds_stats[name]

    # Цветные переменные для итоговой статистики раундов
    wins_str = f"{Colors.GREEN}{r_stats['wins']}{Colors.RESET}"
    losses_str = f"{Colors.RED}{r_stats['losses']}{Colors.RESET}"
    draws_str = f"{Colors.YELLOW}{r_stats['draws']}{Colors.RESET}"

    print(f"{medal} {Colors.BOLD}{name}{Colors.RESET}")
    print(f"   • Выиграно матчей: {Colors.GREEN}{match_wins}{Colors.RESET} из 4")
    print(f"   • Статистика раундов: Побед: {wins_str} | Поражений: {losses_str} | Ничьих: {draws_str}")

print(f"{Colors.YELLOW}{Colors.BOLD}" + "=" * 65 + f"{Colors.RESET}")
