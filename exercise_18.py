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
    
    playing = True

    # from here on out, continue asking until 
    number = random_num()

    # from here on out continue asking
    while playing:
        guess = get_num()

        cows = find_cows(guess, number)
        #bulls = find_bulls

        #if compare() == true:

    


def random_num():               # creates random 4 digit number
    number = []

    for x in range(4):
        number.append(randint(0,10))

    return number

def get_num():
    guess = str(input("Enter your guess: "))

    return guess

def find_cows(guess, number):
    cows = 0
    for i in range(0, 4):
        if number[i] == guess[i]:
            cows += 1
    
    return cows
        


if __name__ == '__main__':          # if 
        main()