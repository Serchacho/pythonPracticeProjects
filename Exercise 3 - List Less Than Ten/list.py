"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""


print()
totalNum = int(input("How many numbers would you like in the list?: "))

list = []    #initializes a list


# random() provides random float values from [0,1)
# randint() provides random integer values from [start number, end number]

for x in range(totalNum):
    temp = int(input("Type any whole number: "))
    list.append(temp)

numCheck = int(input("Numbers printed should be lower than: "))
for x in list:
    if x < numCheck:
        print(x)