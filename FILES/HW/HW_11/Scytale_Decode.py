CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"


def decode(k):
    with open("Result", "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) < 2:
        print(f"{RED}Данні ще не були зашифровані!")
    else:
        coded_t = lines[0].rstrip('\n')
        correct_k = int(lines[1].rstrip('\n'))

        if k == correct_k:
            final_result = ""
            col = len(coded_t) // correct_k
            for collum in range(col):
                for sym in range(collum, len(coded_t), col):
                    final_result += coded_t[sym]

            print(f"{GREEN}Закодована інформація (по ключу {k}):")
            print(f"{YELLOW}{final_result.rstrip(' ')}{RESET}")

        else:
            print(f"{RED}Введено неправильний ключ доступу!")
            print(f"Дані будуть видалені з погляду безпеки!{RESET}")
            with open("Result", "w", encoding="utf-8") as f:
                pass


key = int(input(f"{BRIGHT_BLUE}Введіть числовий ключ для зашифрованого тексту: {RESET}"))

decode(key)
