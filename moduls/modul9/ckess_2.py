n = int(input("Введіть розмір однієї клітинки: "))
s = str(input("Введіть символ для друку: "))
for nub in range(4):
    for j in range(n):
        print()
        for i in range(4):
            print((s + " " * n) * (n - 1) + s, end="")
            print((" " * n) * (n - 1)+" " * n,end="")
    for j in range(n):
        print()
        for i in range(4):
            print((" " * n) * (n - 1)+" " * n,end="")
            print((s + " " * n) * (n - 1) + s, end="")