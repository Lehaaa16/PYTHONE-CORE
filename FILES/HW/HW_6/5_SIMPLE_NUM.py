n = int(input("Введіть число: "))
if n < 2:
    print(f"Число {n} не є простим")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"Число {n} не є простим")
            break
    else:
        print(f"Число {n} є простим")
