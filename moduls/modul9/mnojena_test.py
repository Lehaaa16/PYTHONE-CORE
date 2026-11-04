import random
score = 0
maxn = 5
minn = 1
for i in range(10):
    a = random.randint(minn, maxn)
    b = random.randint(minn, maxn)
    maxn += 3
    if i == 5:
        minn = -10
    ans = int(input(f"{a} * {b} = "))
    if ans == a * b:
        score += 1
print(f"Ваш рахунок: {score}")