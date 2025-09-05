total=0
x=int(input("Введите начальное число: "))
y=int(input("Введите конечное число: "))+1
for i in range(x, y):
    total+=i
    print("Сумма чисел: ", total)
input("Нажмите Enter, чтобы выйти...")