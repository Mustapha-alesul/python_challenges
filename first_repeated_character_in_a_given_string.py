'''
Python program to find the first repeated character in a given string
where the index of the first occurrence is smallest.
'''
string=input('enter a word:\t')
string=string.lower()
def first_repeated_character(word):
    temp=''
    for element in word:
        if word.count(element)<=1:
            if element not in temp:
                temp+=element
            elif element in temp:
                print(f'The first repeated character of {word} is:',element)
                break
            else:
                print(f'There is no repeated character in {word}')
        else:
            print(f'The first repeated character of {word} is:', element)
            break
first_repeated_character(string)