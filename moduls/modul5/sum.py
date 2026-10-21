n=input("Введіть число: ")
s=0
for i in n:
    s+=int(i)
if s%2==0:
    print("Сума цифр парна!")
elif s%2!=0:
    print("Сума цифр не парна!")