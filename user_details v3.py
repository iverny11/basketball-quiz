#Define the function
def user_details(name):
    print("Hello", name)
#Determine if the input only consists of string, if no ask user to input only letters
while True:
    name = input("Please Enter Your Name : ").upper()
    if name.isalpha():
        break

    else:
        print("==============================")
        print("Please Enter Only Letters A-Z")
        print("==============================")


user_details(name)
        
         

