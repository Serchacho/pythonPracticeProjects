"""
Exercise 15 - Reverse Word Order

Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 

For example, say I type the string:
"My name is Kevin"

I get back:
"Kevin is name My"
"""

def reverse_sentence (sentence):

    temp = sentence.split()                                 #.split() without any 'string' inside will just split at the spaces of the sentence
    result = []

    for index in range(0, len(temp)):
        #print(len(temp) - 1 - index)
        result.append( temp[len(temp) - 1 - index] )        # adds elements from temp starting at the end going to the start

    result = " ".join(result)

    return result



sentence = input("Please type a sentence: ")
sentence = reverse_sentence(sentence)
print("Sentence backwards is: " + str(sentence))
print()