def mt(a, b, c, d):
    mn = a
    if b > mn:
        mn = b
    if c > mn:
        mn = c
    if d > mn:
        mn = d
    return mn

print(mt(1, 3, -6, 4))
