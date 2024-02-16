"""
Exercise 14 - List Remove Duplicates

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

import random

def random_elements(length, limit):                     # function to randomly place values into array specified by user
    arr = [random.randint(0, limit + 1) for x in range(0, length)]
    return arr

def remove_duplicates(arr1, arr2):                      # function to remove duplicates using for loops

    custom = [y for x in arr1 for y in arr2 if x==y]    # intializes custom array

    instances = 0

    for x in custom:                                    # traverses through both arrays
        for y in custom:
            if x == y:                                    # if similar numbers, makes sure it only gets added once
                instances += 1
                if instances > 1:
                    custom.pop(custom.index(y))         # removes the second instance of a number in custom array
        instances = 0                                   # once finishes checking, makes sure next number is checked the same

    return custom

def remove_duplicates_set(arr1, arr2):                  # function to remove duplicates using sets (much easier and less confusing)
    array1 = set(arr1)
    array2 = set(arr2)
    custom = array1.intersection(array2)                #set1.intersection(set2) returns values present in BOTH sets
    custom = list(custom)                               #converts custom from set into list
    return custom



length = int(input("Please input how long you want both arrays to be: "))
limit = int(input("Please input the largest value you want in both arrays: "))

a = random_elements(length, limit)
b = random_elements(length, limit)


# output
print()
print("Array a: " + str(a))
print("Array b: " + str(b))
print("Array custom: " + str(remove_duplicates(a,b)))
print("Array set: " + str(remove_duplicates_set(a,b)))
print()