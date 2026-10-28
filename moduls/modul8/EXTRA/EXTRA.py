t=str(input("Введіть рядок: "))
print(t)
for i in range(len(t)):
    s = t[i]
    n = 0
    for j in range(len(t)):
        if s == t[j]:
            n+=1
    print(f"Кількість '{s}' в '{t}': {n}")