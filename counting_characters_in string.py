
''' a Python program to count repeated characters in a string.
# string: a variable to store an entered string
#temp: a variable to store checked characters
#counter: a variable to store repeated time a character is
'''
string=input('enter string to check repeated characters')
string=string.replace(' ','')
temp=''
str1=string
counter=0
for i in str1:
    if i not in temp:

        counter=str1.count(i)
        if counter<=1:
            continue
        else:
            print(i,counter)
            temp=temp+i
    else:
        continue
