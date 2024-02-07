"""
Exercise 16 - Password Generator

Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import string                                           # imports ascii
import random

numbers = [i for i in range(1,10)]                      # creates list with numbers from 1-9
lowerLet = [chr(i) for i in range(97,123)]          # all lower case letters
upperLet = [chr(i) for i in range(65,90)]           # all upper case letters
symbols = [chr(i) for i in range(33,48)]                # chr(i) returns character in ASCII at integer i; 33-47 for symbols

# convert all lists into sets
"""
numbers = set(numbers)
lowerLet = set(lowerLet)
upperLet = set(upperLet)
symbols = set(symbols)
"""

print("This program helps to create a unique password for you.")
include = input("What would you like to include? \n1 - numbers \n2 - lowercase letters \n3 - uppercase letters \n4 - symbols \nPlease include spaces inbetween numbers: ")
include = include.split()                               # removes the spaces inbetween numbers and creates list of them
print(include)
# set of available characters
available = []
#available = set(available)



for num in include:
    if int(num) == 1:
        available.extend(numbers)
    if int(num) == 2:
        available.extend(lowerLet)
    if int(num) == 3:
        available.extend(upperLet)
    if int(num) == 4:
        available.extend(symbols)



# creating password
length = int(input("How long do you want the password?: "))     # determines length of password
password = ''

characters = [available[random.randint(0,len(available))] for i in range(0, length)]        # grabs random element inside of available[] for the length user requested

for char in characters:
    password += str(char)

# display
print("Here is your new password!: " + password)