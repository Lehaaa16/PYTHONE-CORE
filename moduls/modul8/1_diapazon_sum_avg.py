a=int(input("Введіть першу межу: "))
b=int(input("Введіть другу межу: "))
s=0
if a > b:
    a,b = b,a
n = b - a + 1
for i in range(a,b+1):
    s+=i
print(f"Сума чисел від {a} до {b} це {s}\n"
      f"Середнє арефметичне чисел від {a} до {b} це {round(s/n,2)}")
