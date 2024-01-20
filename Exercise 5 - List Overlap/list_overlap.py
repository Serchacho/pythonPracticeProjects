"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

#import random number
from random import randint

#declaring variables
a = []
b = []
c = []
instances = int(0)
index = int(0)


#input for numbers per list
length1 = int(input("Length of list 1: "))
length2 = int(input("Length of list 2: "))

#adding random values to lists
for x in range(1, length1 + 1):
    a.append(randint(1, 10))
for x in range(1, length2 + 1):
    b.append(randint(1, 10))


# first creates list with all common numbers
for x in a:
    for y in b:
        if x == y:
            c.append(x)

# then finds any duplicates
for x in c:
    for y in c:
        if x == y:
            instances += 1
            if instances > 1:
                c.pop(c.index(y))
    
    instances = 0           #after done checking for duplicates with a number, clears instances, then moves to next number
    
print("List 1: " + str(a))
print("List 2: " + str(b))
print("List of common numbers: " + str(c))