#define the function
def user_details():
            print("Hello", name, ". Welcome to the Basketball Quiz!")
while True:
    name = input("Please Enter Your Name: ")
    if name.isalpha():
        break

    else:
        print("Please Enter Only Letters")

user_details()
