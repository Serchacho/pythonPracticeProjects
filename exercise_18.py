"""
Exercise 18 - Cows And Bulls

Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user 
guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in 
the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user 
makes throughout teh game and tell the user at the end.
"""

from random import randint

def main():
    
    number = random_num()


    


def random_num():               # creates random 4 digit number
    number = str()

    for x in range(4):
        number += str(randint(0,10))

    return number

def compare(guess, number):
    print()


if __name__ == '__main__':          # if 
        main()