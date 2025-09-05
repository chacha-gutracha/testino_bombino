while True:
    while True:
        N=input("enter number-> ")
        if N.lower()=="exit":
            break
        try:
            n=(N)
            n=int(n)
            print("произведение ", n*3)
        except ValueError:
            print("пиши правильно!")
    while True:
        F=input("enter fraction number-> ")
        if F.lower()=="exit":
            break
        try:
            f=float(F)
            print(int(f))
        except ValueError:
            print("пиши правильно!")