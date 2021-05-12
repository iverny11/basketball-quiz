#instructions v2

while True:
   
    inst = input("Would you like to read the instructions?\n a)Yes\n b)no\n ")
   
    if inst == 'Yes' or inst == 'yes' or inst == 'A' or inst == 'a' or inst == 'Y' or inst == 'y' :
        print("The instructions are simple...")
        break
    if inst == 'No' or inst == 'no' or inst == 'B' or inst == 'b' or inst == 'n' or inst == 'N' :
        print("Welcome to Isaac's basketball quiz, have fun!")
        break
    else:
        print("**************************************")
        print("Please enter the options provided only")
        print("**************************************")

