CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"


def s_c(t: str, k: int):
    txt = ""
    padding = (k - len(t) % k) % k
    t = t + " " * padding

    for col_num in range(k):
        for symbol in range(col_num, len(t), k):
            txt += t[symbol]

    return txt


print(f"\t\t{BOLD}{CYAN}=== Програма шифрування методом Скитала ==={RESET}\n")

text = input(f"{BRIGHT_BLUE}Будь ласка, введіть вихідне повідомлення для шифрування: ")
key = int(input(f"Введіть числовий ключ (діаметр стержня / кількість стовпців): {RESET}"))

result = s_c(text, key)
with open("Result", "w", encoding="utf-8") as f:
    f.write(f"{str(result)}\n")
    f.write(str(key))

print(f"\n\t\t{BOLD}{YELLOW}=== Результат шифрування успішно збережено! ==={RESET}")
