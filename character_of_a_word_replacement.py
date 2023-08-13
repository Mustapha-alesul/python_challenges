'''
a Python program to replace each character of a word of length five and more with a hash character (#).
'''
sentence=input('enter a sentence')
list=sentence.split(' ')
print(list)
def replacement(list1):
    for element in list1:
        length=len(element)
        if length<5:
            print(element,end=' ')
        else:
            print('#'*length,end=' ')
replacement(list)