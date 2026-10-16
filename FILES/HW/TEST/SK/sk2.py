n=int(input("Write a number: "))
s=str(input("Write a symbol: "))
c=int(input("Write a number of spaces: "))
for i in range(1,n+1):
    print((" "*(c+1))*(n-i),end="")
    ns=s+(" "*c)
    print(ns*((2*i)-1))
#В цій версії можна задати симаол для друку та кількість пробілів між символами