import random

red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
reset = "\033[0;0m"

dif = [(1, 5), (2, 10), (5, 15), (-5, 20), (-10, 25), (-20, 30), (-30, 40), (-40, 45), (-50, 50), (-100, 100)]
ques = len(dif)
score = 0

for i in range(ques):
    minn, maxn = dif[i]
    a = random.randint(minn, maxn)
    b = random.randint(minn, maxn)
    cor_ans = a * b
    while True:
        try:
            ans = int(input(f"{blue}{a} * {b} = "))
            break
        except ValueError:
            print(f"{yellow}Ви ввели не число!{reset}")
            continue
    if ans == cor_ans:
        score += 1
        print(f"{green}Правильно!{reset}")
    else:
        print(f"{red}Неправильно! Правильна відповідь {a * b}! {reset}")
print(f"\n{blue}Ваш рахунок {score}/{ques}")
