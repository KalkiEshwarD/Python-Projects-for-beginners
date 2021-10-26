import random
# imports the random module

LB = int(input("Enter Lower Bound: "))                  # The random numbers that the computer generates will fall under these two bounds LB and UB
UB = int(input("Enter Upper Bound: ")) + 1
number = random.randrange(LB, UB, 1)                    # the function used to create a random number within a specific range.

def the_guess(guess, turns, number):                    # A function I have created to make the work easier. It takes in 3 parameters, the last one, the random number generated is a constant. The rest two keep changing.
    if guess == number:
        print(f"Congratulations you got it in {turns + 1} turns.")                  
    else:
        if guess > number:                                          # this if statement helps the user understand if his guess is bigger or smaller and helps him/her take a better guess.
            print("Your guess is greater than the number.")
        else:
            print("Your guess is smaller than the number.")         
       
        print("Try again")
        the_guess(int(input("Take another guess: ")), turns + 1, number)                    # every time the user gets it wrong the number of turns keeps increasing by 1 and the function gets called again.

the_guess(int(input("Take your first guess: ")), 0, number)                 # I am calling the function with turns = 0 and the first guess as input from the user.
