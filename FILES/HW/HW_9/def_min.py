def def_min(a, b, c, d, e):
    minn = a
    if b < a:
        minn = b
    elif c < b:
        minn = c
    elif d < c:
        minn = d
    elif e < c:
        minn = e
    return minn


print(def_min(1, 8, 12, -5, 0))
