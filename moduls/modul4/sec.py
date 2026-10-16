full_sec=86400
s=int(input("Введіть кількість секунд минувших з 00:00: "))
t=input("\n(sec/min/hr)\nВведіть одиницю часу: ")
if t=="sec":
    print(f"До опівночі залишилось {full_sec-s} секунд")
elif t=="min":
    print(f"До опівночі залишилось {(full_sec-s)/60} хвилин")
elif t=="hr":
    print(f"До опівночі залишилось {(full_sec-s)/3600} годин")
else:
    print("Некоректна одиниця часу!")