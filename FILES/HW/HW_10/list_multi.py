import list


def dob(l):
    d = 1
    for i in range(len(l)):
        d *= l[i]
    return d

print(f"Добуток елементів цього масиву це {dob(list.make())}")