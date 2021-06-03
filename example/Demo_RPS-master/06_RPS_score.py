# RPS Component 6 - End Game Mechanics

import random

# Functions go here


# Round checking function
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

# User choice checking function
def check_choice(question, options):
    valid = False
    while not valid:
        response = input(question)
        response = response.lower()     # make response all lower case

        if response == "xxx":
            return response
        elif response == "r":
            response = "rock"
        elif response == "p":
            response = "paper"
        elif response == "s":
            response = "scissors"

        if response in options:
            return response
        else:
            print("I don't understand...")
            print()


# Heading function

# Main Routine Goes here

# initialise variables
rps_list = ["rock", "paper", "scissors"]
result = ""

# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

end_game = "no"

# Play Game
rounds = check_rounds()

while end_game == "no":
    # Generate computer choice
    comp_choice = random.choice(rps_list)
    print()
    print("Computer Choice: {}".format(comp_choice))
    print()

    # Get user choice

    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        print(heading)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)

        if rounds_played == rounds - 1:
            end_game = "yes"

    user_choice = check_choice("Please choose rock (r), paper (p) or scissors (s): ", rps_list)

    if user_choice == "xxx":
        break

    rounds_played += 1  # This must be AFTER the break otherwise the rounds won calculation will be incorrect.


    # Compare choices
    if comp_choice == user_choice:
        result = "It's a tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "You won!"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "You won!"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "You won!"
    else:
        result = "You lost"
        rounds_lost += 1

    result_statement = "User: {} \t|\t Computer: {} \t|\t Result: {}".format(user_choice, comp_choice, result)

    # Output result
    print(result_statement)

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_played-rounds_drawn-rounds_lost, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")
