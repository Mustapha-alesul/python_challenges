'''
Write a Python program to remove all characters except a specified character from a given string
'''
sentence=input('enter a sentence or a word')
remained=input('enter a character which will remain')
def remove_all_characters(sentencee,character):
    corrected=''
    for element in sentencee:
        if element.upper()==element or element.lower()==character:
            corrected+=element
        else:
            continue
    print(corrected)
remove_all_characters(sentence,remained)