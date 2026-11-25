from moduls.modul_13.cipher.colours import Colors
from cipher import encrypt

print(f"{Colors.BOLD}{Colors.BLUE}=== Читання та розшифрування з файлу ==={Colors.RESET}")

try:
    with open("secret.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Перевіряємо, чи файл не порожній і містить обидва рядки
    if len(lines) < 2:
        print(f"{Colors.RED}Помилка: файл 'secret.txt' пошкоджений або порожній.{Colors.RESET}")
    else:
        saved_key = int(lines[0].strip())  # Перший рядок — збережений ключ
        encoded_text = lines[1]  # Другий рядок — зашифрований текст

        print(f"{Colors.CYAN}Знайдено зашифроване повідомлення: {Colors.BOLD}{encoded_text}{Colors.RESET}")

        while True:
            try:
                user_key = int(input(f"{Colors.YELLOW}Введіть ключ для розшифрування: {Colors.RESET}"))
                break
            except ValueError:
                print(f"{Colors.RED}Помилка: ключ повинен бути цілим числом.{Colors.RESET}")

        if user_key == saved_key:
            decoded_text = encrypt(encoded_text, -user_key)
            print(f"{Colors.GREEN}Доступ дозволено. Розшифрований текст: {Colors.BOLD}{decoded_text}{Colors.RESET}")
        else:
            print(f"{Colors.RED}Помилка доступу: введено невірний ключ!{Colors.RESET}")

except FileNotFoundError:
    print(f"{Colors.RED}Помилка: файл 'secret.txt' не знайдено. Спочатку запустіть encoder.py.{Colors.RESET}")
