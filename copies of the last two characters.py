'''
 a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
'''
sentence=input('enter a word:')
def make_a_copy(word):
    last_two_chars=''
    index=0
    length=len(word)
    if length<2:
        print('''you've inserted few characters
please enter atleast two character''')
    else:
        for element in word:

            if index==length-1 or index==length-2:
                last_two_chars+=element
                index+=1
            else:
                index+=1
        print(last_two_chars*4)

make_a_copy(string)
