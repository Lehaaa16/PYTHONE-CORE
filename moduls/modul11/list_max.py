def mof(l):
    m = l[0]
    for i in range(1, len(l)):
        if l[i] > m:
            m = l[i]
    return m


print(mof([7, 2, 3, 4, 5, 6]))
