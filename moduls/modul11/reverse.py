from list_make import list_make

GREEN = '\033[92m'


def rev(l):
    b = list(l)
    for i in range(len(l)):
        l[i] = b[len(l) - i - 1]
    print(f"{GREEN}{l}")


rev(list_make())
