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
    
    array = []

    for number in range(1, amount):
        #array.append(number + num1 + num2)