lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    n = int(input("Введіть ваш номер: "))
    index = n % len(lst) - 1
    print(lst[index])
