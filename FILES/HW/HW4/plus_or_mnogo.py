a=int(input("Введіть перше число: "))
b=int(input("Введіть друге число: "))
c=int(input("Введіть третє число: "))
d=str(input("\n(+ *)\nВведіть дію: "))
if d=="+":
    print(f"{a} + {b} + {c} = {a+b+c}")
elif d=="*":
    print(f"{a} * {b} * {c} = {a*b*c}")
else:
    print(f"Некоректа дія!")