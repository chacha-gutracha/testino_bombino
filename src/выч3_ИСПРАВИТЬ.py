while True:
    seconds=int(input("Enter the number of seconds: "))
    hours=seconds//3600
    minutes=seconds//60
    if seconds>=3600:
        minutes=minutes//60
    seconds=seconds%60
    print(f"{hours} hours, {minutes} minutes and {seconds} seconds")