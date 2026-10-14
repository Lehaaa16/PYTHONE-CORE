a=int(input("Ввеіть перше число: "))
b=int(input("Ввеіть друге число: "))
k=str(input("\n(+, -, *, avg)\nВведіть дію: "))
if k=="+":
    print(f"{a} + {b} = {a+b}")
elif k=="-":
    print(f"{a} - {b} = {a-b}")
elif k=="*":
    print(f"{a} * {b} = {a*b}")
elif k=="avg":
    print(f"({a}+{b})/2 = {(a+b)/2}")
else:
    print("Некоректний оператор!")