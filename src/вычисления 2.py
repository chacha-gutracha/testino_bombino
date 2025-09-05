while True:
    print("Разность квадратов")
    a=float(input("Введите а: "))
    b=float(input("Введите b: "))
    c=((a+b)*(a-b))
    print(c)
    x=3
    y=7
    x,y=y,x
    print(x, y)
    klusha=3#тема с операторами
    klusha+=2
    klusha*=4
    print(klusha)
    q,z,w=4,6,8
    print(q-z+w)
    pi=3.14159
    print(round(pi, 2))#округление до двух знаков после запятой
    print(5/2, type(5/2))#нормальное деление
    print(5//2, type(5//2))#деление без остатка