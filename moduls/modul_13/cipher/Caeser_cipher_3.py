import languages
from colours import Colors

alphabets = [
    languages.ukr_low,
    languages.ukr_up,
    languages.eng_low,
    languages.eng_up
]


def encrypt(text, key):
    txt = ""
    for char in text:
        found = False
        for alpha in alphabets:
            if char in alpha:
                pos = alpha.index(char)
                new_pos = (pos + key) % len(alpha)
                txt += alpha[new_pos]
                found = True
                break
        if not found:
            txt += char
    return txt


l_encoded = ""
l_key = None

# Стартова інструкція (жирний блакитний заголовок + бірюзовий опис команд)
print(f"\t\t\t{Colors.BOLD}{Colors.BLUE}=== Програма шифрування (Шифр Цезаря) ==={Colors.RESET}")
print(f"{Colors.CYAN}Доступні команди:")
print("  • Введіть звичайний текст — для шифрування")
print("  • /decode                 — для розшифрування останнього повідомлення")
print("  • /decode <текст>         — для розшифрування довільного тексту")
print(f"  • /exit                   — для завершення роботи\n{Colors.RESET}")

while True:
    t = input(f"{Colors.YELLOW}Введіть текст або команду: {Colors.RESET}")

    if t == "/exit":
        print(f"{Colors.BLUE}Роботу програми завершено.{Colors.RESET}")
        break

    try:
        k = int(input(f"{Colors.YELLOW}Введіть ключ (ціле число): {Colors.RESET}"))
    except ValueError:
        print(f"{Colors.RED}Помилка вводу: ключ повинен бути цілим числом.\n{Colors.RESET}")
        continue

    if t == "/decode":
        if l_encoded == "":
            print(f"{Colors.RED}Помилка: у пам'яті відсутній зашифрований текст.\n{Colors.RESET}")
        elif k == l_key:
            decoded = encrypt(l_encoded, -k)
            print(f"{Colors.GREEN}Розшифрований текст: {Colors.BOLD}{decoded}\n{Colors.RESET}")
        else:
            print(f"{Colors.RED}Помилка доступу: вказано невірний ключ.\n{Colors.RESET}")

    elif t.startswith("/decode "):
        custom_text = t[8:]
        decoded = encrypt(custom_text, -k)
        print(f"{Colors.GREEN}Результат розшифрування: {Colors.BOLD}{decoded}\n{Colors.RESET}")

    else:
        l_encoded = encrypt(t, k)
        l_key = k
        print(f"{Colors.GREEN}Зашифрований текст: {Colors.BOLD}{l_encoded}\n{Colors.RESET}")
