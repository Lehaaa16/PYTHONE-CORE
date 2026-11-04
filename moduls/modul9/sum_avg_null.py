while True:
    print("\tsum - Сума чисел \n\tavg - Середнє чисел \n\tnull - Кількість нулів \n\texit - Вийти з програми")
    d = str(input("Виберіть опцію: "))
    if d == "exit":
        break
    n = str(input("Введіть велике число: "))
    if d == "sum":
        s = 0
        for i in n:
            s += int(i)
        print(f"Сума чисел дорівнює {s}")
    elif d == "avg":
        s = 0
        for i in str(n):
            s += int(i)
        print(f"Середнє арефметичне чисел дорівнює {s / len(n)}")
    elif d == "null":
        print(f"Кількість нулів дорівнює {round(n.count("0"),2)}")
    else:
        print("Введіть інші данні!")
    print()
