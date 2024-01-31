"""
Exercise 13 - Fibonacci

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""

def fibonacci(amount):
    num1 = int(0)
    num2 = int(0)
    
    array = [0] * amount                    # initializes an array varibale with 0 in every cell with the amount specified by user
    array[0] = 1
    index = int(1)                          # index = 1 because don't want to touch first cell of array

    #for num in range(1, amount):            # sets all values in array, except first cell, to zero
    #    array[num] = 0

    while (index < len(array)):           # adds numbers in 1 and 2 cells before current position
        array[index] = array[index - 1] + array[index - 2]
        index += 1

    return array


length = int(input("How many numbers in the sequence would you like to generate?: "))
custom = fibonacci(length)                  # custom takes value of array with specified number of fibanacci numbers

print("These are the first " + str(length) + " Fibonacci numbers: " + str(custom))
        