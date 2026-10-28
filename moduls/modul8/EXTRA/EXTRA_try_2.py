t=str(input("Введіть рядок: "))
for s in set(t):
    n = t.count(s)
    print(f"Кількість '{s}' в '{t}': {n}")