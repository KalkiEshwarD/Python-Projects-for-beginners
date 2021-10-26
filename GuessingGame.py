import random

LB = int(input("Enter Lower Bound: "))
UB = int(input("Enter Upper Bound: ")) + 1
number = random.randrange(LB, UB, 1)

def the_guess(guess, turns, number):
    if guess == number:
        print(f"Congratulations you got it in {turns + 1} turns.")
    else:
        if guess > number:
            print("Your guess is greater than the number.")
        else:
            print("Your guess is smaller than the number.")
        print("Try again")
        the_guess(int(input("Take another guess: ")), turns + 1, number)

the_guess(int(input("Take your first guess: ")), 0, number)
