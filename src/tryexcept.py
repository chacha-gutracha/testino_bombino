try:
    x=int(input("Введи нуль-> "))
    пытка=10/x
except ValueError:
    print("ты не то вводишь, балбес")
except ZeroDivisionError:
    print("жопу свою подели!")
else: print(пытка)
finally: print("Спасибо за внимание!")