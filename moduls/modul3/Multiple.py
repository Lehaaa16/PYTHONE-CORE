num=int(input("Введіть число: "))
crat=int(input(f"Число якому буде кратне {num}: "))
if num%crat==0:
    print(f"{num} is multiple by {crat}!")
else:
    print(f"{num} isn`t multiple by {crat}!")