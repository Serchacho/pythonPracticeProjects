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

# MAIN FUNCTION

def main():
    
    # intro
    print("This is Cows and Bulls!")
    print("All you have to do is try to guess the 4-digit number \nfrom 1-9 that the computer randomly generated.")
    print("A cow means you guessed the correct number in the correct \nlocation. A bull means you guessed a correct number, but \nin the wrong location.")
    print("Let's play!")
    print()

    # variables
    playing = True
    cows = 0
    bulls = 0
    guesses = 0
    
    
    while playing:                                  # while player wants to continue playing
        number = random_num()
        print("Computer has chosen a number")
        print(number)

        while cows != 4:                            # while player has not gotten 4 cows yet
            guess = get_num()
            guesses += 1

            cows = find_cows(guess, number)
            bulls = find_bulls(guess, number)

            print(str(cows) + " cows, " + str(bulls) + " bulls.")
            print()

        print("You guessed the number!")
        print("It took you " + str(guesses) + " guesses.")
        playing = bool(input("Would you like to try again? yes = 1, no = 0: "))
        print()
        cows = 0
        guesses = 0



# FUNCTIONS

def random_num():               # creates random 4 digit number
    number = []

    for x in range(4):
        number.append(randint(0,9))

    return number


def get_num():
    guess = str(input("Enter your guess: "))
    guess = list(guess)
    for i in range(0,4):
        guess[i] = int(guess[i])

    return guess


def find_cows(guess, number):
    cows = 0
    for i in range(0, 4):
        if number[i] == guess[i]:
            cows += 1
    
    return cows


def find_bulls(guess, number):
    times = 0
    bulls = 0
    for x in number:
        for y in guess:
            if(x == y and number.index(x) != guess.index(y)):
                times = 1

        bulls += times
        times = 0
    
    return bulls



if __name__ == '__main__':          # if the name of a function is 'main' then run it
    main()