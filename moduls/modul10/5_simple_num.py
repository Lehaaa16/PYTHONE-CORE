def s(a):
    for i in range(1, a - 1):
        if a % (a - i) == 0:
            return False
    return True


print(s(37))
