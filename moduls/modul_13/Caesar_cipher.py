lett = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
lett_up = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
k = int(input("Введіть ключ: "))
t = input("Введіть текст: ")


def encrypt(text, key):
    txt = ""
    for char in text:
        if char in lett:
            pos = lett.index(char)
            new_pos = (pos + key) % len(lett)
            txt += lett[new_pos]
        elif char in lett_up:
            pos = lett_up.index(char)
            new_pos = (pos + key) % len(lett_up)
            txt += lett_up[new_pos]
        else:
            txt += char
    return txt


print(encrypt(t, k))
