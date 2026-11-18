def a_s(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    av = round(s / len(l), 2)
    print([s, av])


a_s([1, 3, 7, 4, 574, 123, 78, 24, 82])
