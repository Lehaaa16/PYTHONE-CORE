dol=float(input("Введіть суму в доларах: "))
typ=str(input("\n (EUR,GBR,JPY)\nВиберіть валюту: "))
if typ=="EUR":
    print(f"{dol} Доларів у {typ} це {dol*0.9}")
elif typ=="GBR":
    print(f"{dol} Доларів у {typ} це {dol*0.76}")
elif typ=="JPY":
    print(f"{dol} Доларів у {typ} це {round(dol*158.83,1)}")
else:
    print("Некоректний тип валюти!")
