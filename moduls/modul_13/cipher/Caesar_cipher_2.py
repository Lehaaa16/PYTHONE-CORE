import languages
import colours

alphabets = [
    languages.ukr_low,
    languages.ukr_up,
    languages.eng_low,
    languages.eng_up
]


def encrypt(text, key):  # Метод
    txt = ""  # Створення пустого текстового об'єкта
    for char in text:  # Пошук символа у даному тексті
        found = False  # Задання параметра "знайдений" у положення False
        for alpha in alphabets:  # Перебір алфавітів (англ/укр, великі/маленькі)
            if char in alpha:  # Спроба пошуку символу в алфавіті
                pos = alpha.index(char)  # Задання поточної позиції даного символу в алфавіті
                new_pos = (pos + key) % len(alpha)  # Обчислення нової позиції
                txt += alpha[new_pos]  # Додавання до тексту символу по новому індексу
                found = True  # Задання параметра "знайдений" у положення True
                break  # Вихід з циклу
        if not found:  # Перевірка, чи був знайдений символ
            txt += char  # Якщо ні — додаємо як є
    return txt  # Повернення тексту після всього циклу


l_encoded = ""  # Тут зберігатиметься останній зашифрований текст
l_key = None  # Тут зберігатиметься ключ від нього

while True:
    t = input(f"{colours.Colors.GREEN}Введіть текст: ")
    k = int(input(f"{colours.Colors.BLUE}Введіть ключ: "))

    if t == "/decode":  # Якщо текст "/decode"
        if l_encoded == "":  # Якщо немає минулого зашифрованого тексту (перший ввід)
            print(f"{colours.Colors.RED}Не має зашифрованого тексту!\n")  # Виводимо помилку
        elif k == l_key:  # Якщо ключ збігається з потрібним
            decoded = encrypt(l_encoded, -k)  # Ми записуємо значення в змінну (-k щоби повернути значення до кодування)
            print(colours.Colors.HEADER + decoded + "\n")  # І виводимо
        else:  # Інакше (ключ неправильний)
            print(f"{colours.Colors.RED}Неправильний ключ!\n")  # Виводимо помилку
    else:  # Інакше (текст не "/decode")
        l_encoded = encrypt(t, k)  # Змінюємо значення останнього кодування на результат роботи функції encrypt
        l_key = k  # Останній ключ прирівнюємо до ключа який ми ввели
        print(colours.Colors.HEADER + l_encoded + "\n")  # Вивід результату роботи функції
