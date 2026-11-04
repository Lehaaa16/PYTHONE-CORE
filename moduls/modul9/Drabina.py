n = int(input("Введіть число: "))
for j in range(n):
    print(" " * j * 2, end="")
    for i in range(1, n + 1):
        print(i, end=" ")
    n -= 1
    print()
