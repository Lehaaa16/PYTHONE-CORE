def p():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    if a > b:
        b, a = a, b
    m = 1
    for i in range(a, b + 1):
        m *= i
    print(m)


p()
