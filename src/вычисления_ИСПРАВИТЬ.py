while True:
    while True:
        A=input("Enter first number ")
        if A.lower()=="exit":
            break
        try:
            a=int(A)
        except ValueError:
            print("Enter integer number!")
    while True:
        B=input("Enter second number ")
        if B.lower()=="exit":
            break
        try:
            b=int(B)
        except ValueError:
            print("Enter integer number!")
    print("result of division: ", a/b)
    print("residue", a%b)
    print("result of multiplication: ", a*b)
    print("result of exponentiation: ", a**b)