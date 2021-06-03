while True:
                        inst = input("Would you like to read the instructions?\na)yes\nb)no\nEnter here: ")
                        if inst == "yes" or inst == "y" or inst == "A" or inst == "a":
                                    print("""The instructions are simple, you will be given random multiple choice general
knowledge questions about basketball and you have to choose which answer you think is right.
Answer the multiple choice questions by entering (a/b/c/d). For every question you get right you earn a point.
""")
                                    break
                        if inst == "no" or inst == "n" or inst == "B" or inst == "b" :
                                    print("Welcome to Isaac's basketball quiz")
                                    break
                        else:
                                    print("Please enter the options")
