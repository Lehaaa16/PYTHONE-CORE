from list_make import list_make


def rev(l):
    b = list(l)
    for i in range(len(l)):
        l[i] = b[len(l) - i - 1]
    print(l)


a = list_make()
rev(a)
