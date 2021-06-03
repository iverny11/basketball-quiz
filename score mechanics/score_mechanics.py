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
                        else:
                                    print("Please enter the alphabet for chosen option")
user_answer()
answer()
