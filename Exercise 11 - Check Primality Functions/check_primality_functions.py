"""
Ask the user for a number and determine whether the number is prime or not (For those who have forgotten, a prime number is a number that has no divisors). 
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
"""

def get_integer():
    return int(input("Please give me an integer: "))

def check_prime(num):
    freq = int(0)

    for i in range(1, num + 1):
        if (num % i == 0):
            freq += 1

    if (freq == 2):
        return True
    else:
        return False
    


print("This program checks to see if your number is a prime number")
number = get_integer()

if(check_prime(number)):
    print("Your number is a prime number")
else:
    print("Your number is NOT a prime number")