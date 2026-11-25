import languages

alphabets = [
    languages.ukr_low,
    languages.ukr_up,
    languages.eng_low,
    languages.eng_up
]
t = input("Введіть текст: ")
k = int(input("Введіть ключ: "))


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


print(encrypt(t, k))
