while True:
    try:
        rounds = int(input("\nPlease enter how many rounds you want to paly maximum is 10 rounds : "))
        if 0<rounds<=15:
            break
        else:
            print("Please only enter the rounds 1-10")
        except:
