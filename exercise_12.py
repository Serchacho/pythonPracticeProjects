"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""


def first_and_last(arr):
    custom = []
    custom.append(arr[0])
    custom.append(arr[-1])
    
    return custom

numbers = [1,2,3,4,5]
custom = first_and_last(numbers)

print("Numbers array: " + str(numbers))
print("Custom array: " + str(custom))