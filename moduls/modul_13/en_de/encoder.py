from moduls.modul_13.cipher.colours import Colors
from cipher import encrypt

print(f"{Colors.BOLD}{Colors.BLUE}=== Шифрування та запис у файл ==={Colors.RESET}")

text = input(f"{Colors.YELLOW}Введіть текст для шифрування: {Colors.RESET}")

while True:
    try:
        key = int(input(f"{Colors.YELLOW}Введіть ключ (ціле число): {Colors.RESET}"))
        break
    except ValueError:
        print(f"{Colors.RED}Помилка: ключ повинен бути цілим числом.{Colors.RESET}")

encoded_text = encrypt(text, key)

# Записуємо у файл (encoding="utf-8" обов'язково для коректної роботи з українською мовою)
with open("secret.txt", "w", encoding="utf-8") as file:
    file.write(f"{key}\n")
    file.write(encoded_text)

print(f"{Colors.GREEN}Успішно! Дані зашифровано та збережено у файл 'secret.txt'.{Colors.RESET}")
print(f"{Colors.CYAN}Зашифрований вигляд: {Colors.BOLD}{encoded_text}{Colors.RESET}")
