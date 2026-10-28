a=int(input("Введіть перше значення: "))
b=int(input("Введіть друге значення: "))
if a<=b:
    for i in range(a,b+1,1):
        print(i, end = " ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i, end = " ")