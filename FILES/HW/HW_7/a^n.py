a = int(input("Введіть число: "))
n = int(input("Введіть ступінь: "))
s = 1
if n >=0:
    for i in range(1, n + 1):
        s *= a
    print(s)
else:
    n*=-1
    for i in range(1, n + 1):
        s *= a
    print(f"1/{s}")