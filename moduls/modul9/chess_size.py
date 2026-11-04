n = int(input("Введіть розмір однієї клітинки: "))
s = str(input("Введіть символ для друку: "))
for nb in range(1, 4 + 1):
    for i in range(n):
        for l in range(4):
            print((s + " " * n) * n, end="")
#            print(" " * n, end="")
        print()
    for i in range(n):
        for q in range(4):
#            print(" " * n, end="")
            print((s + " " * n), end="")
        print()