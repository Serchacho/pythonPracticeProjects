"""
Description: Program finds the simplified version of the square root of a number
"""

def main():
    num = int(input("Input number: "))
    
    simplified(num)
    



def simplified(num):

    original = num
    maxSquare1 = 1
    maxSquare2 = 1

    for x in range(1,num + 1):
        if(num % (x*x) == 0 and x*x > maxSquare1):
            maxSquare1 = x
    
    num /= (maxSquare1*maxSquare1)
    num = int(num)

    # runs a second time to see if there are any squares left
    for x in range(1, num + 1):
        if(num % (x*x) == 0 and x*x > maxSquare2):
            maxSquare2 = x
    
    num /= (maxSquare2*maxSquare2)
    num = int(num)

    print("sqrt(", original, ") simplified is:", maxSquare1*maxSquare2, "sqrt(", num, ")")



    



if __name__ == '__main__':
    main()