while True:
    name=input("Write your name: ")
    input("...")
    print(f"Hello, my dear {name}! It is very important sciense program for number analysis!")
    input("...")
    response=input("Do you have degree of doctor of mathematical sciences? ->")
    if response.lower()in["yes", "yeah", "ye"]:
        while True:
            numik=input("enterino numerino->")
            if numik.lower()=="exit":
                break
            try:
                numero=int(numik)
                if numero==0:
                    print("null")
                else: print("ne null")
            except ValueError:
                print("It's not valid numerino!")
    elif response.lower()in["да","дыа","дя"]:
        print("eta proga dlya anglichan!")
    else: print("pashol nahui")
    x=input("Start again? Press Enter. If you want to exit, type 'fuck down'->")
    if x.lower()=="fuck down":
        break