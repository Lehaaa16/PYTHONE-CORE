def line(l,d,s):
    if d=="hor":
        print(f"{s} "*l)
    elif d=="ver":
        for i in range(l):
            print(s)
line(5,"hor","*")