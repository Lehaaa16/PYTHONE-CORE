t=str(input("Введіть рядок: "))
for s in set(t):
    print(f"Кількість '{s}' в '{t}': {t.count(s)}")