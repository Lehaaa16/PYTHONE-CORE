while True:
    n = int(input("Введіть число: "))
    if n == 7:
        print("Я не люблю 7, допобачення!")
        break
    elif n > 0:
        print(f"Число {n} - позитивне!")
    elif n < 0:
        print(f"Число {n} - негативне!")
    else:
        print("Це нуль!")
