while True:
    print("\n\t а/б/в/г")
    n = str(input("Виберіть варіант замальовки: "))

    for i in range(1, 6):
        print("*  " * i + "   " * (11 - 2 * i) + "*  " * i)

    for i in range(5, 0, -1):
        print("*  " * i + "   " * (11 - 2 * i) + "*  " * i)

    else:
        print("Будь ласка, введіть коректний варіант (а, б, в, г).")
