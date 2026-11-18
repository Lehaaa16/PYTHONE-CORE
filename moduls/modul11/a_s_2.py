from list_make import list_make


def a_s(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    av = round(s / len(l), 2)
    print(f"Сума: {s}\nСереднє: {av}")


a_s(list_make())
