from list_make import list_make


def mof(l):
    m = l[0]
    for i in range(1, len(l)):
        if l[i] > m:
            m = l[i]
    print(f"Максимальне число змасиву: {m}")


mof(list_make())
