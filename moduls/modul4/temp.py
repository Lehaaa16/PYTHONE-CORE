t=int(input("Введіть температуру: "))
if t<-10:
    print("Дуже холодно!")
elif (t>=-10) and (t<0):
    print("Холодно!")
elif (t>=0) and (t<15):
    print("Прохолодно!")
elif (t>=15) and (t<25):
    print("Тепло!")
elif t>25:
    print("Дуже тепло!")
else:
    print("Некоректний час!")
