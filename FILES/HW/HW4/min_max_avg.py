a=int(input("Введіть перше число: "))
b=int(input("Введіть друге число: "))
c=int(input("Введіть третє число: "))
d=str(input("\n( min / max / avg )\nВведіть оператора: "))
if d == "min":
    print((a, b, c))
elif d == "max":
    print(max(a,b,c))
elif d == "avg":
    print(round((a+b+c)/3,2))
else:
    print("Помилковий оператор!")