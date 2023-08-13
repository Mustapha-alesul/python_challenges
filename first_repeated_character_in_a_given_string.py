'''
Python program to find the first repeated character in a given string
where the index of the first occurrence is smallest.
'''
string=input('enter a word:\t')
def first_repeated_character(word):
    temp=''
    for element in word:
        if element not in temp:
            temp+=element
        elif element in temp:
            print(f'The first repeated character of {word} is:',element)
            break
        else:
            print(f'There is no repeated character in {word}')
first_repeated_character(string)