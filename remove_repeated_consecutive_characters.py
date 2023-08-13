'''
a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string
'''
sentence=input('enter a sentence')
list=sentence.split(' ')
def remove_repeaeted(list1):
    temp=''
    corrected=''
    for element in list1:
        for sub in element:
            if temp==sub:
                continue
            else:
                corrected+=sub
                temp=sub
        corrected+=' '
    print(corrected,end=' ')

remove_repeaeted(list)