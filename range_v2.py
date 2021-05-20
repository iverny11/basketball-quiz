#define the function
def rounds():
            global r, total
            while True:
                        try:
                                    r = int(input("Please enter the number of questions you would like to answer between 1-10: "))
                                    if 0<r<=10:
                                                break
                                    else:
                                                print("Please enter numbers 1-10 only")
                        except:
                                    print('Please enter numbers only')

            total = r
