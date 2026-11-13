def pol(n):
    for i in range(len(n)):
        if n[i] == n[len(n) - i - 1]:
            continue
        else:
            return False
    return True


num = input("Введіть число: ")
print(pol(num))
