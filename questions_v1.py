correct = "\n********\nCorrect!\n********"
incorrect= "\n##########\nIncorrect!\n##########"
A1 = "2"
A2 = "3"
A3 = "James Naismith"
A4 = "10"
A5 = "NBA"
A6 = "Michael Jordan"
A7 = "1"
A8 = "Layup"
A9 = "10 feet"
A10 = "2"

score = 0 

#Question 1
answer = input("How many steps can you take without dribbling? \nA. 1 \nB. 2 \nC. 4 \nD. 7 \nPlease enter a answer: ")

if answer == "B" or answer == "2" or answer == "b":
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A1)
    print ("Score is:",score)
    print("\n")           

#Question 2
answer = input("How many points is a 3 pointer worth?  \nA. 2 \nB. 7 \nC. 3 \nD. 4 \nPlease enter a answer: ")

if answer == "C" or answer == "3" or answer == "c":
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A2)
    print ("Score is:",score)
    print("\n")           

#Question 3
answer = input("Who invented basketball?  \nA. Jerry West \nB. John Smith \nC. Michael Jordan \nD. James Naismith \nPlease enter an answer: ").upper()

if answer == "D" or answer == "James Naismith" or answer == "d":
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A3)
    print ("Score is:",score)
    print("\n")           

#Question 4
answer = input("How many players in total can be on the court at the same time  \nA. 3 \nB. 2 \nC. 5 \nD. 10 \nPlease enter an answer: ")

if answer == "D" or answer == "10" or answer == "d":
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A4)
    print ("Score is:",score)
    print("\n")

#Question 5
answer = input("What is the best basketball league in the world?  \nA. NBA \nB. NBL \nC. WNBA \nD. CBA \nPlease enter an answer: ").upper()

if answer == "A" or answer == "nba" or answer == "a" or answer == "NBA" :
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A5)
    print ("Score is:",score)
    print("\n")

#Question 6
answer = input("Who is the most iconic basketball player of all time?  \nA. LeBron James \nB. Michael Jordan \nC. Kobe Bryant \nD. Stephen Curry \nPlease enter an answer: ").upper()

if answer == "B" or answer == "Michael Jordan" or answer == "b" or answer == "michael jordan" :
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A6)
    print ("Score is:",score)
    print("\n")

#Question 7
answer = input("How many points is a free throw worth?  \nA. 3 \nB. 2 \nC. 4 \nD. 1 \nPlease enter an answer: ")

if answer == "D" or answer == "1" or answer == "d" or answer == "one" :
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A7)
    print ("Score is:",score)
    print("\n")

#Question 8
answer = input("What is the easiest way to score in basketball?  \nA. Layup \nB. Free throw \nC. 3 Pointer \nD. Floater \nPlease enter an answer: ").upper()

if answer == "A" or answer == "Layup" or answer == "a" or answer == "layup" :
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A8)
    print ("Score is:",score)
    print("\n")

#Question 9
answer = input("How high is a normal basketball hoop?  \nA. 11 feet \nB. 9 feet \nC. 10 feet \nD. 5 feet \nPlease enter an answer: ").upper()

if answer == "C" or answer == "10 feet" or answer == "c" or answer == "10 Feet" :
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A9)
    print ("Score is:",score)
    print("\n")

#Question 10
answer = input("How many points is a layup worth?  \nA. 2 \nB. 1 \nC. 4 \nD. 3 \nPlease enter an answer: ")

if answer == "A" or answer == "2" or answer == "a" or answer == "two" :
    score += 1
    print(correct)
    print ("Score is:",score)
    print("\n")
else:
    print(incorrect)
    print("The correct answer is :" ,A10)
    print ("Score is:",score)
    print("\n")



#Final Message
if score <= 1:
    print("Your score is:",score,"try again next time")
else:
    print("Your score is:",score,"Nice you got a good score!")
    
