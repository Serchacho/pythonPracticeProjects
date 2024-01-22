"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""



print("This program checks to see if the word you put in is a palindrome")
word = input("Please enter a word: ")

index = int(0)
same = True

for s in word:
    if s != word[-1-index]:
        same = False
    index += 1

if same == True:
    print("This word is a palindrome")
else:
    print("Sorry, this word is NOT a palindrome")