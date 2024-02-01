"""
Exercise 14 - List Remove Duplicates

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def remove_duplicates(arr1, arr2):
    custom = []            # intializes custom array

    notDupe = True

    for x in arr1:          # traverses through both arrays
        for y in arr2:
            if x==y and notDupe:    # if similar numbers, makes sure it only gets added once
                custom.append(y)
                notDupe = False
            
        notDupe = True              # once finishes checking, makes sure next number is checked the same

    return custom

a = [1,2,3,4,5,6,7,8,9,1]
b = [1,5,7,11,4,5,1]


print(remove_duplicates(remove_duplicates(a,b), b))