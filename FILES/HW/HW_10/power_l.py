import list


def power_list(n, p):
    res = []
    for item in n:
        res.append(item ** p)
    return res


l = list.make()
p = int(input("Введіть ступінь: "))
print(f"Результат: {power_list(l, p)}")
