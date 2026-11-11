def lucky(a):
    l, r = 0, 0
    for i in range(0, 3):
        l += int(str(a)[i])
    for i in range(3, 6):
        r += int(str(a)[i])
    if l == r:
        return True
    else:
        return False


print(lucky(123510))
