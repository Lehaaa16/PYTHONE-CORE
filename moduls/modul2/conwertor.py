a=int(input("Введіть суму: "))
t=str(input("Виберіть валюту (USD/EUR/PLN/TRY): "))
if (t=="USD"):
    print(f"{a} Доларів в грн це {a*44.86}")
elif(t=="EUR"):
    print(f"{a} Євро в грн це {a*50.15}")
elif(t == "PLN"):
    print(f"{a} Злотих в грн це {a * 11.48}")
elif (t == "TRY"):
    print(f"{a} Лір в грн це {a * 0.91}")
else:
    print("Неправильний тип валюти!")
