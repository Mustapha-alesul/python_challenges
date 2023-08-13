'''
a Python program to print the index of a character in a string
'''
word=input('enter a word to check its characters indeces')
counter=0
for element in word:
    print(element,counter)
    counter+=1
