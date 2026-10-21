a=input("Введіть шестизначне число: ")
if len(a)==6:
    n1, n2 = 0,0
    for i in range(len(a)):
        if i <= 2:
            n1 += int(a[i])
        elif i > 2:
            n2 += int(a[i])
    if n1 == n2:
        print("Щасливе")
    else:
        print("Нещасливе")
else:
    print("Некоректна інформація!")