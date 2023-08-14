'''
 a Python program to get the last part of a string before a specified character.
'''
string=input('enter a word')
character=input('enter a specific character')
def get_the_last_part(word,characterr):
    correct=''
    for element in word:
        if element!=characterr:
            correct+=element
        else:
            break
    print(correct)
get_the_last_part(string,character)