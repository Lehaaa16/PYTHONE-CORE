a=int(input("Введіть першу межу: "))
b=int(input("Введіть другу межу: "))
print("1 - зростання\n2 - спадання")
p=int(input("Введіть порядок: "))
if p == 2:
    for i in range(max(a,b), min(a,b) - 1, -1):
        print(i)
elif p == 1:
    for i in range(min(a,b), max(a,b) + 1, +1):
        print(i)