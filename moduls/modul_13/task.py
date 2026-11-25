while True:
    n = int(input("Введіть ваш номер: "))
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = n % len(lst)
    print(lst[n - 1])
