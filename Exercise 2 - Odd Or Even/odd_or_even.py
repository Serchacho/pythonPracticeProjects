"""
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""

#print("This program will check to see if the number you input is odd or even.")
print("This program is to see whether the number you input is odd or even, see if it is a multiple of 4, as well as")
print("to see if your number is a factor of the second number you provide.")
num1 = int(input("Please input your first number: "))
num2 = int(input("Please input your second number: "))



if num1 % 2 == 0:           #if num1 is even
    print("The number " + str(num1) + " is even")

    # check if num1 is factor of 4
    if num1 % 4 == 0:
        print("And the number " + str(num1) + " is a factor of 4")
    else:
        print("And the number " + str(num1) + " is NOT a factor of 4")

    #check if num1 is divisible by num2
    if num1 % num2 == 0:
        print("And the number " + str(num1) + " is a factor of " + str(num2) + ".")
    else:
        print("And the number " + str(num1) + " is NOT a factor of " + str(num2) + ".")
elif num1 % 2 == 1:         #if num1 is odd
    print("The number " + str(num1) + " is odd")

    # check if num1 is factor of 4
    if num1 % 4 == 0:
        print("And the number " + str(num1) + " is a factor of 4")
    else:
        print("And the number " + str(num1) + " is NOT a factor of 4")

    #check if num1 is divisible by num2
    if num1 % num2 == 0:
        print("And the number " + str(num1) + " is a factor of " + str(num2) + ".")
    else:
        print("And the number " + str(num1) + " is NOT a factor of " + str(num2) + ".")
else:
    print("ion know man...")