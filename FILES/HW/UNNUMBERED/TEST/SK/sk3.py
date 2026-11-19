e=int(input("Write an end amount: "))
s=str(input("Write a symbol: "))
c=int(input("Write a number of spaces: "))
if e%2==0:
    e-=1
    print(f"Here is your pyramid with base of {e} (rounded to the nearest odd number):")
else:
    print(f"Here is your pyramid with base of {e}:\n")
for i in range(1,e+1,2):
    print(" "*((c+1)*(e-i)//2),end="")
    print((s+(" "*c))*i)
#Ця версія схожа на минулу, тільки замість кількості рядків, ми вводимо кінцеву кількіть символу (на нижньому рядку)