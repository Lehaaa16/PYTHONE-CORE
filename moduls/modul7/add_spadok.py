a=int(input("Введіть першу межу: "))
b=int(input("Введіть другу межу: "))
for i in range(max(a,b), min(a,b) - 1,-1):
    if i % 2 == 0:
        print(i, end = " ")