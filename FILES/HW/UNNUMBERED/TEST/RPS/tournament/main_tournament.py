from agents.SlidingAnalyst import SlidingAnalyst
from agents.CumulativeAnalyst import CumulativeAnalyst
from agents.CounterAnalyst import CounterAnalyst
from agents.TitForTat import TitForTat
from agents.Stubborn_human import StubbornHuman
from agents.HumanRandom import HumanRandom
from agents.PureRobot import PureRobot


# ANSI-коди для красивого кольорового виведення в консолі
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
    elif (m1 == "камінь" and m2 == "ножиці") or \
         (m1 == "ножиці" and m2 == "папір") or \
         (m1 == "папір" and m2 == "камінь"):
        return "p1"
    else:
        return "p2"


def play_match(player1, player2, games_count):
    p1_wins = 0
    p2_wins = 0
    local_draws = 0

    # Скидання стану перед матчем для всіх можливих атрибутів ботів
    for p in (player1, player2):
        if hasattr(p, 'opponent_history'): p.opponent_history = []
        if hasattr(p, 'my_history'): p.my_history = []
        if hasattr(p, 'counts'): p.counts = {"камінь": 0, "ножиці": 0, "папір": 0}
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


# --- ІНТЕРАКТИВНЕ ВВЕДЕННЯ КІЛЬКОСТІ ІГОР ---
print(f"{Colors.YELLOW}{Colors.BOLD}=== НАЛАШТУВАННЯ ТУРНІРУ З КАМІНЬ-НОЖИЦІ-ПАПІР ==={Colors.RESET}")
print(f"{Colors.GREEN}У турнірі беруть участь 7 ботів. Усього буде зіграно 21 парна дуель.{Colors.RESET}")
user_input = input(f"{Colors.BLUE}Введіть кількість матчів для однієї дуелі: {Colors.RESET}")

try:
    games_per_duel = int(user_input)
except ValueError:
    games_per_duel = 1000
    print(f"{Colors.RED}Введено не число! Автоматично встановлено значення за замовчуванням: 1000.{Colors.RESET}")

total_all_games = games_per_duel * 21
print(f"\n{Colors.RED}{Colors.BOLD}⚠️ УВАГА: Оскільки учасників 7, усього пройде 21 парна дуель.")
print(f"Загальна кількість зіграних раундів у всьому турнірі складе: {total_all_games} ({games_per_duel} × 21){Colors.RESET}\n")

input(f"{Colors.HEADER}{Colors.BOLD}Натисніть Enter, щоб запустити турнір...{Colors.RESET}")

# Опис учасників
print(f"\n{Colors.HEADER}{Colors.BOLD}" + "=" * 80)
print(" 🤖 УЧАСНИКИ ТУРНІРУ ТА ЇХНІ СТРАТЕГІЇ:")
print("=" * 80 + f"{Colors.RESET}")
print(f"1. {Colors.BOLD}Майстер-Аналітик{Colors.RESET}: Аналізує останні 10 ходів суперника (ковзне вікно).")
print(f"2. {Colors.BOLD}Динамічний Накопичувач{Colors.RESET}: Збільшує шанс контр-ходу на +1% за раунд (до 80%).")
print(f"3. {Colors.BOLD}Контр-Аналітик{Colors.RESET}: Стратег другого порядку, що прораховує кроки аналітиків наперед.")
print(f"4. {Colors.BOLD}Наслідувач{Colors.RESET}: Реалізує тактику 'Око за око' (Tit-for-Tat) — копіює минулий хід.")
print(f"5. {Colors.BOLD}Упертюх (Камінь){Colors.RESET}: Людина з перекосом характеру, що обожнює камінь (60%).")
print(f"6. {Colors.BOLD}Звичайна людина{Colors.RESET}: Симулює людську психологію (Win-Stay / Lose-Shift).")
print(f"7. {Colors.BOLD}Робот-Рандомайзер{Colors.RESET}: Класичний чистий рандом (33%/33%/33%).\n")

# Список усіх учасників (7 ботів)
players_classes = [
    lambda: SlidingAnalyst("Майстер-Аналітик"),
    lambda: CumulativeAnalyst("Динамічний Накопичувач"),
    lambda: CounterAnalyst("Контр-Аналітик"),
    lambda: TitForTat("Наслідувач"),
    lambda: StubbornHuman("Упертюх (Камінь)"),
    lambda: HumanRandom("Звичайна людина"),
    lambda: PureRobot("Робот-Рандомайзер")
]

# Статистика: перемоги в матчах та загальні очки
match_scores = {cls().name: 0 for cls in players_classes}
total_rounds_stats = {cls().name: {"wins": 0, "losses": 0, "draws": 0} for cls in players_classes}

print(f"{Colors.HEADER}{Colors.BOLD}" + "=" * 80)
print(" 🏆 ПОЧАТОК КРУГОВОГО ТУРНІРУ 🏆")
print("=" * 80 + f"{Colors.RESET}\n")

n = len(players_classes)

# Коловий турнір
for i in range(n):
    for j in range(i + 1, n):
        p1 = players_classes[i]()
        p2 = players_classes[j]()

        w1, w2, match_draws = play_match(p1, p2, games_per_duel)

        # Збираємо статистику раундів
        total_rounds_stats[p1.name]["wins"] += w1
        total_rounds_stats[p1.name]["losses"] += w2
        total_rounds_stats[p1.name]["draws"] += match_draws

        total_rounds_stats[p2.name]["wins"] += w2
        total_rounds_stats[p2.name]["losses"] += w1
        total_rounds_stats[p2.name]["draws"] += match_draws

        print(f"{Colors.CYAN}⚔️ Дуель:{Colors.RESET} {Colors.BOLD}{p1.name}{Colors.RESET} vs {Colors.BOLD}{p2.name}{Colors.RESET}")

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

        draws_str = f"Нічиїх: {Colors.YELLOW}{match_draws}{Colors.RESET}"

        print(f"    Результат -> {p1_str} | {p2_str} | {draws_str}\n")

print(f"{Colors.YELLOW}{Colors.BOLD}" + "=" * 80)
print(" 👑 ПІДСУМКОВА ТАБЛИЦЯ ЛІДЕРІВ ТУРНІРУ:")
print("=" * 80 + f"{Colors.RESET}")

# Сортуємо спочатку за виграними матчами, а при рівності — за сумою перемог у раундах
sorted_leaderboard = sorted(
    match_scores.items(),
    key=lambda item: (item[1], total_rounds_stats[item[0]]["wins"]),
    reverse=True
)

medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]

for rank, ((name, match_wins), medal) in enumerate(zip(sorted_leaderboard, medals), 1):
    r_stats = total_rounds_stats[name]

    # Кольорові змінні для підсумкової статистики раундів
    wins_str = f"{Colors.GREEN}{r_stats['wins']}{Colors.RESET}"
    losses_str = f"{Colors.RED}{r_stats['losses']}{Colors.RESET}"
    draws_str = f"{Colors.YELLOW}{r_stats['draws']}{Colors.RESET}"

    print(f"{medal} {Colors.BOLD}{name}{Colors.RESET}")
    print(f"   • Виграно матчів: {Colors.GREEN}{match_wins}{Colors.RESET} із 6")
    print(f"   • Статистика раундів: Перемог: {wins_str} | Поразок: {losses_str} | Нічиїх: {draws_str}")

print(f"{Colors.YELLOW}{Colors.BOLD}" + "=" * 80 + f"{Colors.RESET}")