import math
r=int(input("Введіть радіус кола: "))
f=input("P or S: ")
if f=="S":
    print(f"Площа кола з радіусом {r} це {round(math.pi * r * r,2)}")
elif f=="P":
    print(f"Периметр кола з радіусом {r} це {round(2 * math.pi * r,2)}")
else:
    print("Некортекто введено обчислювальну змінну!")