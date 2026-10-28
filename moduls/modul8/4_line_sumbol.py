n=int(input("Введіть число: "))
s=str(input("Введіть символ: "))
if n>=0:
    for i in range(n):
        print(s,end="")
else:
    print(f"Неможливо намалювати лінію довжиною {n}!")