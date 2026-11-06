while True:
    print("\n\t а/б/в/г/д/е/ж/з/и/к")
    n = str(input("Виберіть варіант замальовки: "))
    if n == "а":
        for i in range(10):
            print("   " * i + "*  " * (10 - i))
    elif n == "б":
        for i in range(1, 11):
            print("*  " * i)
    elif n == "в":
        for i in range(6):
            print("   " * i + "*  " * (11 - 2 * i))
    elif n == "г":
        for i in range(6):
            print("   " * (5 - i) + "*  " * (2 * i + 1))
    elif n == "д":
        for i in range(6):
            print("   " * i + "*  " * (11 - 2 * i))
        for i in range(1, 6):
            print("   " * (5 - i) + "*  " * (2 * i + 1))
    elif n == "е":
        for i in range(1, 6):
            print("*  " * i + "   " * (11 - 2 * i) + "*  " * i)
        print("*  *  *  *  *  *  *  *  *  *  *")
        for i in range(5, 0, -1):
            print("*  " * i + "   " * (11 - 2 * i) + "*  " * i)
    elif n == "ж":
        for i in range(1, 7):
            print("*  " * i)
        for i in range(5, 0, -1):
            print("*  " * i)
    elif n == "з":
        for i in range(1, 7):
            print("   " * (11 - i - 5) + "*  " * i)
        for i in range(5, 0, -1):
            print("   " * (11 - i - 5) + "*  " * i)
    elif n == "и":
        for i in range(10):
            print("*  " * (10 - i))
    elif n == "к":
        for i in range(10, 0, -1):
            print("   " * (i - 1) + "*  " * (11 - i))
    elif n == "закінчити":
        print("\tКінець виконання програми")
        break
    else:
        print("\tf"
              "Будь ласка, введіть коректний варіант")
