"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

from random import randint

"""
quit = input("Would you like to play (again)? yes or no\n")
while quit != "yes":
    print("while loop")
"""


print("This program plays a rock, paper, scissors game versus the computer")
#player = input("Please input a choice; rock, paper, or scissors")
player = input("Please input a choice; 1=rock, 2=paper, or 3=scissors.\nPlayer choice: ")

# make computer make random decision from 1-3 and then changes it to a string
computer = int(randint(1,4))

if computer == 1:
    computer = str("rock")
elif computer == 2:
    computer = str("paper")
elif computer == 3:
    computer = str("scissors")
else:
    print("Computer doesn't have a decision")

print("Computer choice: " + computer + "\n")


# figure out who won
if player == "rock" and computer == "scissors":
    print("PLayer won! " + str(player) + " beats " + str(computer) + ".\n")
elif player == "paper" and computer == "rock":
    print("PLayer won! " + str(player) + " beats " + str(computer) + ".\n")
elif player == "scissors" and computer == "rock":
    print("PLayer won! " + str(player) + " beats " + str(computer) + ".\n")
elif player == computer:
    print("It's a tie! Both you and the computer chose " + player + ".\n")
else:
    print("Sorry, the computer won. " + computer + " beats " + player + ".\n")


