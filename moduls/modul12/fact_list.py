from math import factorial

from moduls.modul11.list_make import list_make


def l_f(l):
    li = []
    for i in range(len(l)):
        li.append(factorial(l[i]))
    print(li)


l_f(list_make())
