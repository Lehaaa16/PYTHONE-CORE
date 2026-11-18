def list_make():
    l = []
    i = 0

    while True:
        val = input(f"Введіть {i + 1} елемент масиву (або Enter для завершення): ")
        if val == "":
            break
        l.append(int(val))
        i += 1
    return l
