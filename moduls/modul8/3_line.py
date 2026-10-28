n=int(input("Введіть число: "))
if n>=0:
    for i in range(n):
        print("*",end="")
else:
    print(f"Неможливо намалювати лінію довжиною {n}!")