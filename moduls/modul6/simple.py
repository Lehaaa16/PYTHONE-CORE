n=int(input("Введіть число: "))
p = True
for num in range(1,n+1):
    p = True
    for i in range(2,num):
        if num % i == 0:
            p = False
            break
    if p:
        print(num, end="\n")