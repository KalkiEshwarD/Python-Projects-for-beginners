# Here I have created a rock, paper scissor game, but it proved to be rather difficult. Took me quite a while.
# The code you see below is definitely not the most efficient, but it gets the job done.
# I have taken three functions to play this game, choice, clash, and score. The behaviour of the functoins are rather intuitive.
# The choice function takes in the chioce of the user and generates a computer choice. It takes in no arguments.
# The clash function takes in the user choice and the computer choice and then calculates the result.
# The score function takes in the argument result and also maintains the score. It also halts the game if the maximum score has been reached.
# The whole code first flows into the choice function then into the clash and finally into the score function before starting again at the choice function.
# CHOICE -----> CLASH -----> SCORE -----> CHOICE.
# There are definitely ways to improve the code, and make sure you try to do so. If you find a way to reduce the number of lines I've taken, try and send over the code. I'll try to improve mine.


import random
max = int(input("What is the maximum score you would like to play?"))                   # Sets the maximum score
options = '1.Rock \n2.Paper \n3.Scissor'                                                # Displays the options to user
computer_score = 0                                                                      # Sets initial value of scores to 0
human_score = 0



def choice():                                                                           # Creates function choice that 
    
    print(options)
    user_choice = int(input("What do you play?\n"))
    if user_choice not in range(1, 4):
        print("Invalid Choice")
        choice()
    comp_choice = random.randrange(1, 4, 1)                                             # Uses my favourite randrange attribute to choose a random number
    clash(comp_choice, user_choice)

    
    
def score(result):

    global computer_score                                                               # The problem is variables don't work as global variables in function unless they are declared as such.
    global human_score                                                                                  

    if result == 'Draw':                                                                # This block handles the score assignment and management.
        computer_score += 0.5
        human_score += 0.5
    elif result == 'Win':
        human_score += 1
    elif result == 'Lose':
        computer_score +=1
    print("Your score: ", human_score, "\nComputer score: ", computer_score)

    if computer_score == max and computer_score == human_score:                         # This block handles the program when to stop.
        print("Draw")
    elif human_score == max:
        print("You win!")
    elif computer_score == max:
        print("Computer Wins")
    else:
        choice()

        
        
def clash(computer_choice, human_choice):                                               # This is the clash function which covers different cases which could occur.
    
    if computer_choice == 1:
        print("I choose Rock")                                                      
        if human_choice == 1:
            score('Draw')                                                               # Sets the result and initiaties the score funciton.
        elif human_choice == 2:
            score("Win")
        elif human_choice == 3:
            score("Lose")

    elif computer_choice == 2:
        print("I choose Paper")
        if human_choice == 1:
            score("Lose")
        elif human_choice == 2:
            score("Draw")
        elif human_choice == 3:
            score("Win")
            
    elif computer_choice == 3:
        print("I choose Scissors")
        if human_choice == 1:
            score("Win")
        elif human_choice == 2:
            score("Lose")
        elif human_choice == 3:
            score("Draw")
        
            
            
choice()                                                    # At last, calls upon the choice function.
