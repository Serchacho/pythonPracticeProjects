"""
Input:  1. terms
        2. values of terms
        
"""


def main():
    num_terms = 0
    factor = 0
    num_terms = int(input("How many terms are there?: "))
    terms = []

    for i in range(0, num_terms):
        print("term #", i+1, ": ")
        num = int(input())
        terms.append(num)
    
    print(terms)

    for r in range(0, 100):
        result = 0

        for power in range(num_terms-1, -1, -1):
            result += pow(r, power)*terms[power]
        #result = pow(r, 3)*terms[0] + pow(r, 2)*terms[1] + r*terms[2] + terms[3]
        if(result == 0):
            factor = r
        
        r = -r
        result = 0
        for power in range(num_terms-1, -1, -1):
            result += pow(r, power)*terms[power]
        #result = pow(r, 3)*terms[0] + pow(r, 2)*terms[1] + r*terms[2] + terms[3]
        if(result == 0):
            factor = r

    print("a factor of the equation is (r +", -1 * factor, ")")    




if __name__ == '__main__':
    main()