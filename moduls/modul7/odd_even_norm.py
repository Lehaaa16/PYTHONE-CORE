a=int(input("Введіть першу межу: "))
b=int(input("Введіть другу межу: "))
c=min(a,b)
d=max(a,b)
print(f"Всі парні числа від {c} до {d} по зростанню:")
for i in range(c, d + 1, +1):
    if i % 2 == 0:
        print(i,end = " ")
print(f"\nВсі непарні числа від {c} до {d} по спаданню:")
for i in range(d, c - 1, -1):
    if i % 2 != 0:
        print(i,end = " ")