a = int(input("Введіть першу межу: "))
b = int(input("Введіть другу межу: "))
if a > b:
    a, b = b, a
d = 1
for i in range(a, b + 1):
    if i % 4 == 0 and i % 6 != 0:
        d *= i
if d == 1:
    print(f"Чисел що виконують умову немає в діапазоні {a} - {b}!")
else:
    print(d)