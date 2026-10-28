t=str(input("Введіть рядок: "))
for i in range(len(t)):
    s = t[i]
    n = t.count(s)
    print(f"Кількість '{s}' в '{t}': {n}")