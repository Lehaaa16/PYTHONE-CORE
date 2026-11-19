import list


def del_s(l, d):
    n = 0
    print(f"\nПочатковий список : {l}")
    while d in l:
        l.remove(d)
        n += 1
    print(f"Фінальний список : {l}")
    print(f"Кількість видалених елементів: {n}")


l = list.make()
d = int(input("Виберіть символ для видалення: "))

del_s(l, d)
