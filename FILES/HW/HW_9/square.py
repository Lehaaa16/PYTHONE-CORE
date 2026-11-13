def square(l, s, b):
    if b == 1:
        for j in range(l):
            print(f"{s}  " * l)
    else:
        for i in range(l):
            if i == 0 or i == l - 1:
                print(f"{s}  " * l)
            else:
                print(f"{s}  " + "   " * (l - 2) + s)
    print("\n")


square(15, "*", 1)
square(10, "#", 0)
