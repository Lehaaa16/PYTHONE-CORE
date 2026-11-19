def syma(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s


while True:
    n1 = int(input("Введіть перше число: "))
    n2 = int(input("Введіть друге число: "))
    print(f"Сума всіх чисел від {n1} до {n2} це {syma(n1, n2)}")
