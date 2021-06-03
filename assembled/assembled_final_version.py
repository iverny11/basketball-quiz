from random import shuffle

#define the function
def user_details():
            print("Hello", name, ". Welcome to the Basketball Quiz!")
while True:
    name = input("Please Enter Your Name: ").capitalize()
    if name.isalpha():
        break

    else:
        print("Please Enter Only Letters")
       
#define the function
def instructions():
            while True:
                        inst = input("Would you like to read the instructions?\na)yes\nb)no\nEnter here: ")
                        if inst == "yes" or inst == "y" or inst == "A" or inst == "a" or inst == "Yes":
                                    print("""\nThe instructions are simple, you will be given random multiple choice 
questions about basketball and you have to choose which answer you think is right.
Answer the multiple choice questions by entering (a/b/c/d). For every question you get right you earn a point.
""")
                                    break
                        if inst == "no" or inst == "n" or inst == "B" or inst == "b" or inst == "No" :
                                    print("Welcome to Isaac's basketball quiz")
                                    break
                        else:
                                    print("Please enter the options")
#define the function
def status():
            status = input("Would you like to play the quiz?\nEnter y to continue or n to exit the quiz : ").lower()
            if status == "y" or status == "yes":
                        print("Thank you, we shall begin the General Knowledge Basketball Quiz shortly. \n")
            else:
                        print("Thank you for taking the time to use my program.")
                        exit()

#define the function
def rounds():
            global r, total
            while True:
                        try:
                                    r = int(input("Please enter the number of questions you would like to answer (between 1-10): \n"))
                                    if 0<r<=10:
                                                break
                                    else:
                                                print("Please enter numbers 1-10 only")
                        except:
                                    print('Please enter numbers only')

            total = r


#using dictionaries in order to store the questions, choices, and answers
quiz = [
["How many steps can you take without dribbling?",
 {'answer' : 'b', 'choice' : ' \nA. 1 \nB. 2 \nC. 4 \nD. 7\n'}
 ],
["How many points is a 3 pointer worth? ",
 {'answer' : 'c', 'choice' : ' \nA. 2 \nB. 7 \nC. 3 \nD. 4 \n'}
 ],
["Who invented basketball?",
 {'answer' : 'd', 'choice' : ' \nA. Jerry West \nB. John Smith \nC. Michael Jordan \nD. James Naismith \n'}
 ],
["How many players in total can be on the court at the same time?",
 {'answer' : 'd', 'choice' : ' \nA. 3 \nB. 2 \nC. 5 \nD. 10 \n'}
 ],
["What is the best basketball league in the world?",
 {'answer' : 'a', 'choice' : '\nA. NBA \nB. NBL \nC. WNBA \nD. CBA \n'}
 ],
["Who is the most iconic basketball player of all time?",
 {'answer' : 'b', 'choice' : '\nA. LeBron James \nB. Michael Jordan \nC. Kobe Bryant \nD. Stephen Curry \n'}
 ],
["How many points is a free throw worth?",
 {'answer' : 'd', 'choice' : '\nA. 3 \nB. 2 \nC. 4 \nD. 1 \n'}
 ],
["What is the easiest way to score in basketball?",
 {'answer' : 'a', 'choice' : '\nA. Layup \nB. Free throw \nC. 3 Pointer \nD. Floater \n'}
 ],
["How high is a normal basketball hoop?",
 {'answer' : 'c', 'choice' : '\nA. 11 feet \nB. 9 feet \nC. 10 feet \nD. 5 feet \n'}
 ],
["How many points is a layup worth?",
 {'answer' : 'a', 'choice' : '\nA. 2 \nB. 1 \nC. 4 \nD. 3 \n'}
 ],


]

shuffle(quiz)

index = 0
score = 0
optnum = 0

user_details()
instructions()
status()
rounds()
print("\nNOTE: during the quiz if you would like to exit, please enter xxx as a answer \n")

while r>0:
            data = quiz[0]
            q = data[0]
            data = data[1]
            answer = data['answer']
            choice = data['choice']

            print(q)
            print(choice)
            while True:
                        user_answer = input ("Please enter one of the options (a/b/c/d): ").lower().replace(' ','')
                        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
                                    if user_answer == answer:
                                               print("\n-----------------------------\nYou are correct, good job!\n-----------------------------\n")
                                               score +=1
                                               print("your score is", score)
                                    else:
                                                print("\n********************\nYou are incorrect!\n********************\n")
                                                print("your score is still",score)

                                    del quiz[0]
                                    r-=1
                                    break
                        elif user_answer == 'xxx':
                                  exit()
                        else:
                                    print("Please enter the letter for the chosen option")
print("You have succesfully completed Isaac's Basketball Quiz!")
print(name,"your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing\n")
while True:
        try:

                  feedback = int(input("How would you rate the quiz from 1-5?:"))
                  if 0<feedback<6:
                           break
                  else:
                           print("Please enter numbers 1-5")
        except:
                  print("Please enter an integer")
print("Thank you for the feedback!")
exit()
