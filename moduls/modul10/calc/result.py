import calc

def get_num(text):
    while True:
        try:
            return int(input(f"{blue}{text}: {reset}"))
        except ValueError:
            print(f"{red}Ви ввели не число! {reset}")

operations = {
    "+": calc.sum,
    "-": calc.minus,
    "*": calc.mult,
    "/": calc.div,
    "^": calc.power,
    "√": calc.root,
    "%": calc.modul,
    "//": calc.integer
}

blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
purple = "\033[35m"
reset = "\033[0;0m"

while True:
    print(f"{yellow}+ - * / ^ √ % //")
    o = str(input(f"{purple}Виберіть операцію: {reset}"))
    if o == "/end":
        print(f"\t{purple}Вихід з циклу...")
        break

    a = get_num("Введіть перше число")
    b = get_num("Введіть друге число")
    print(f"{green}{operations[o](a, b)}{reset}\n")