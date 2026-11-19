import list


def easy(num):
    if num < 2:
        return None
    for i in range(2, num):
        if num % i == 0:
            return None
    return num


def s_l(l):
    r_l = []
    num = 0
    for i in l:
        n = easy(i)
        if n is not None:
            r_l.append(n)
            num += 1
    print(f"Всі прості числа з масиву: {r_l}")
    print(f"Кількість простих чисел з масиву: {num}")



s_l(list.make())
