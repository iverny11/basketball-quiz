#this is version 2
def user_details(name,age):
    print("Hello", name, "and your age is", age)


while True:
    name=input("What is your name? : ")
    if name.isalpha():
        break
    print("Please enter characters A-Z only")
age = input("What is your age? : ")
user_details(name,age)
