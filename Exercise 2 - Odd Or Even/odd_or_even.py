"""
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""

print("This program will check to see if the number you input is odd or even.")
num = int(input("Input a number: "))

# input validation
#while isinstance(num, (str, float, dict, list, tuple)):
#    num = input("Sorry, that didn't work. Please input a number: ")

if num % 2 == 0:
    print("The number " + str(num) + " is even")
elif num % 2 == 1:
    print("The number " + str(num) + " is odd")
else:
    print("ion know man...")