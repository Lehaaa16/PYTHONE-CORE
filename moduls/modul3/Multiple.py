num=int(input("Введіть число: "))
crat=int(input(f"Число якому буде кратне {num}: "))
if num%crat==0:
    print(f"{num} is multple by {crat}!")
else:
    print(f"{num} isn`t multple by {crat}!")