BLUE = '\033[94m'
RESET = '\033[0m'


def make():
    l = []
    i = 0

    while True:
        val = input(f"Введіть {i + 1} елемент масиву {BLUE}(Enter для завершення): {RESET}")
        if val == "":
            break
        l.append(int(val))
        i += 1
    return l