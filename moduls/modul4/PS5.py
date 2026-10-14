cost=float(input("Введіть вартість однієї приставки: "))
num=int(input("Введіть кількість: "))
dis=float(input("Введіть відсоток знижки: "))

print(f"Ціна: {round((cost*num)-((cost*num)*(dis/100)))}")