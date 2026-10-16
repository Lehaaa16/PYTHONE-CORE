h=int(input("Введіть години: "))
if (h>=0) and (h<6):
    print("Доброї ночі!")
elif (h>=6) and (h<13):
    print("Доброго ранку!")
elif (h>=13) and (h<17):
    print("Доброго дня!")
elif (h>=17) and (h<24):
    print("Доброго вечора!")
else:
    print("Некоректний час!")
