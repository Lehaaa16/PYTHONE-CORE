import languages

alphabets = [
    languages.ukr_low,
    languages.ukr_up,
    languages.eng_low,
    languages.eng_up
]
t = str(input("Введіть текст: "))
k = int(input("Введіть ключ: "))


def encrypt(text, key):
    txt = ""                                                # Створення пустого текстового об'єкта
    for char in text:                                       # Пошук символа у даному тексті
        found = False                                       # Задання параметра "знайдений" у положення False
        for alpha in alphabets:                             # Перебір алфавітів(англ/укр, великі/маленькі)
            if char in alpha:                               # Спроба пошуку символу в алфавіті
                pos = alpha.index(char)                     # Задання поточної позиції даного символу в тексті
                new_pos = (pos + key) % len(alpha)          # Обчислення нової позиції
                txt += alpha[new_pos]                       # Додавання до тексту символу по новому індексу
                found = True                                # Задання параметра "знайдений" у положення True
                break                                       # Вихід з циклу
        if not found:                                       # Перевірка чи був знайдений символ
            txt += char                                     # Якщо ні - додаємо як є
    return txt                                              # Повернення тексту після всього циклу


print(encrypt(t, k))
