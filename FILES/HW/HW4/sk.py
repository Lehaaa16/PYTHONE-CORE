n=int(input("Write a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*((2*i)-1))
#Найпростіша версія, є тільки введення кількості поверхів