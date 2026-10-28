a=int(input("Введіть першу межу: "))
b=int(input("Введіть другу межу: "))
c=min(a,b)
d=max(a,b)
for i in range(c, d + 1):
    if i % 2 != 0:
        print(i, end = " ")