a=int(input("Введіть номер місяця: "))
if a == 12 or a == 1 or a == 2:
    print("Зима")
elif 3 <= a <= 5:
    print("Весна")
elif 6 <= a <= 8:
    print("Літо")
elif 9 <= a <= 11:
    print("Осінь")
else:
    print("Некоректні дані!")