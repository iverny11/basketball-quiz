#instructions v3

while True:
   
    inst = input("Would you like to read the instructions?\n a)Yes\n b)no\nEnter here: ")
   
    if inst == 'Yes' or inst == 'yes' or inst == 'A' or inst == 'a' or inst == 'Y' or inst == 'y' or inst == 'YES' :
        print("The instructions are simple, you will be given random multiple choice questions about basketball and you have to choose which answer you think is right. ")
        break
    if inst == 'No' or inst == 'no' or inst == 'B' or inst == 'b' or inst == 'n' or inst == 'N' or inst =='NO':
        print("Welcome to Isaac's basketball quiz, have fun!")
        break
    else:
        print("**************************************")
        print("Please enter the options provided only")
        print("**************************************")
