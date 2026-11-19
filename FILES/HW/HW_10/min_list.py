import list


def m(l):
    mi=l[0]
    for i in l:
        if i<mi:
            mi=i
    return mi
print(f"{m(list.make())}")
