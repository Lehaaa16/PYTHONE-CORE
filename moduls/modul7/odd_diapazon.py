a=int(input("Введіть першу межу: "))
b=int(input("Введіть другу межу: "))
if a <= b:
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end = " ")
elif a > b:
    for i in range(a, b - 1,-1):
        if i % 2 != 0:
            print(i, end = " ")