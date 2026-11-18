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
    print(f"\tЗагалом: {len(l)}")
    print(f"{GREEN}Парних: {even}\n{RED}Непарних: {odd}\n{BLUE}Додатніх: {pos}\n{CYAN}Від'ємних: {neg}")


open([1, -5, -7345, 67, 45, 33, 44, 55, 77, -55, -88, -999])
