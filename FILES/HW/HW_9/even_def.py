def even_def(min, max):
    s = ""
    for i in range(min, max + 1):
        if i % 2 == 0:
            s += str(i) + " "
    return s


print(even_def(11, 35))
