a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
print("\n\t(min / max / avg)")
choice = str(input("Виберіть оператор: "))

if choice == "max":
  ma = a
  if b > ma:
    ma = b
  elif c > ma:
    ma = c
  print(f"Максимальне число: {ma}")
elif choice == "min":
  mi = a
  if b < mi:
    mi = b
  elif c < mi:
    mi = c
  print(f"Мінімальне число: {mi}")
elif choice == "avg":
  av = round((a + b + c) / 3,2)
  print(f"Середнє арифметичне: {av}")
else:
  print("Некоректний оператор!")