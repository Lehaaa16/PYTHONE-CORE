n = int(input("Write a number: "))
l = ""
r = ""
for s in range(1, n + 1):
    print("  " * (n - s), end="")
    for i in range(1, s):
        if i < s:
            l += str(i) + " "
    for i in range(s, 0, -1):
        if i < s:
            r += " " + str(i)
    print(l, end="")
    print(s, end="")
    print(r)
    l, r = "", ""
