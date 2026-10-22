n=int(input("Введіть число від 1 до 100: "))
if 1<=n<=100:
    if n % 3 == 0:
        print("Fizz ",end="")
    if n % 5 == 0:
        print("Buzz",end="")
    else:
        print(n)
else:
    print("Помилка!")