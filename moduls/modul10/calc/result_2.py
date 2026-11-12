import calc
b, g, r, y, p, rst = "\033[0;34m", "\033[0;32m", "\033[0;31m", "\033[0;33m", "\033[35m", "\033[0;0m"
f = lambda t: int(input(f"{b}{t}: {rst}"))
ops = {'+': calc.sum, '-': calc.minus, '*': calc.mult, '/': calc.div, '^': calc.power, '√': calc.root, '%': calc.modul, '//': calc.integer}

while True:
    print(f"{y}+ - * / ^ √ % //")
    o = input(f"{p}Виберіть операцію: {rst}")
    if o == "/end": print(f"\t{p}Вихід..."); break
    print(f"{g}{ops[o](f('Введіть перше число'), f('Введіть друге число'))}{rst}\n" if o in ops else f"{r}Помилка!{rst}")