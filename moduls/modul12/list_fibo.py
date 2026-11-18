from FILES.HW.TEST.RPS.RPS import count
from moduls.modul11.list_make import list_make


def fib(n):
    a, b = 1, 1
    while True:
        a, b = b, a + b
        if n == a:
            return n
        elif n < a:
            return None


f_l = list_make()
l = []
for i in range(len(f_l)):
    f_n = fib(f_l[i])
    if f_n is None:
        continue
    else:
        l.append(f_n)

print(l)
