#define the function
def status():
            status = input("Would you like to play the quiz?\n Enter y to continue or n to exit the quiz : ").lower()
            if status == "y" or status == "yes":
                        print("Thank you, we shall begin the General Knowledge Basketball Quiz shortly. \n")
            else:
                        print("Thank you for taking the time to use my program.")
                        exit()
