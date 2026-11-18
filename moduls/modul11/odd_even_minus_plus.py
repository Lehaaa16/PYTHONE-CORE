from list_make import list_make

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
CYAN = '\033[96m'


def open(l):
    odd, even, pos, neg = 0, 0, 0, 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even += 1
        else:
            odd += 1
        if l[i] > 0:
            pos += 1
        elif l[i] < 0:
            neg += 1
    print(f"\n\tЗагалом: {len(l)}")
    print(f"{BLUE}Парних: {even}\n{CYAN}Непарних: {odd}\n{GREEN}Додатніх: {pos}\n{RED}Від'ємних: {neg}")


open(list_make())
