"""
Exercise 20 - Element Search

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:
Use binary search.
"""

def main():
    numbers = [num for num in range(1, 9)]

    user_num = int(input("Guess a number in the list: "))

    if(compare(numbers, user_num)):
        print("Yes " + str(user_num) + " is inside the list.")
    else:
        print("Sorry, " + str(user_num) + " is not inside the list.")



def compare(numbers, user_num):

    numInside = False

    for num in numbers:
        if num == user_num:
            numInside = True

    return numInside


if __name__ == '__main__':
    main()