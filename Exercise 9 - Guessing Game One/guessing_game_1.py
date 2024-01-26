"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

print("\nGame: Guessing Game One")
print("How to play:")
print("The computer will have a random number, and you have to guess which one it is.\nYou will keep playing until you guess it.")
print()
cont = input("Would you like to play? y or n: ")

while cont == 'y' or cont == 'Y':

    # computer gets number from 1-9
    computer = int(random.randint(1, 10))
    
    # print("Computer num: " + str(computer))       # testing purposes

    player = int(input("Enter a number from 1-9: "))

    while player != computer:

        if player > computer:
            print("Too high! Guess lower.\n")
        elif player < computer:
            print("Too low! Guess higher.\n")
        
        player = int(input("Enter a number from 1-9: "))
    # end of while player != computer
            
    print("Congratulations! You got the right number")

    cont = input("Would you like to play again? y or n: ")
# end of while cont == yes
    
print("Thanks for playing!")

