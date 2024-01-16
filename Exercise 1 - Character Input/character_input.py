"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, 
see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

Input:  1. user's name
        2. user's age
Processing: 1. currentYear = the current year
            2. year100 = 100
            3. finds difference between the users age and the year 100
Output: 1. displays the user's name, age, and when the user will be 100 years old based on current year
"""

print()
print("Hi! This program is going to help you figure out how many years it will take until you are 100 years old.\n")
name = input("First, can I have your name?: ")
age = int(input("\nNow, can I have your age?: "))

print("\nThanks, " + name + ". Your age is " + str(age) + " and you will turn 100 years old in " + str(100-age) + " years.")
print()