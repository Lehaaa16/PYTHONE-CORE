a = int(input("Рівень продажів для першого менеджера: "))
b = int(input("Рівень продажів для другого менеджера: "))
c = int(input("Рівень продажів для третього менеджера: "))
def zp(n1, n2, n3):
    if n1<0 or n2<0 or n3<0:
        print("Помилка: Рівень продажів не може бути від'ємним!")
        exit()
    clear = 0
    if 0 <= n1 <= 500:
        clear = 200 + (n1 / 100 * 3)
    elif 500 < n1 <= 1000:
        clear = 200 + (n1 / 100 * 5)
    elif n1 > 1000:
        clear = 200 + (n1 / 100 * 8)
    if n1 >= n2 and n1 >= n3:
        return clear + 200
    else:
        return clear
print(zp(a, b, c), zp(b, a, c), zp(c, a, b))