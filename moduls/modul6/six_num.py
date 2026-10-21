a=input("Введіть шестизначне число: ")
b=0
if len(a)==6:
    for i in range(len(a)):
        if i != 2 and i != 3:
            b=a[len(a)-i-1]
            print(b, end="")
        else:
            print(a[i],end="")
else:
    print("Некоректна інформація!")