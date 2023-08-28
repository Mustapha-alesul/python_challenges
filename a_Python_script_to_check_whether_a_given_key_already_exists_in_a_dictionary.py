'''
 Write a Python script to check whether a given key already exists in a dictionary.
'''

dictionary = {'hi':'hello','Good':'Morning',5:'five',12:'twelve'}
a_given_key = input('enter any key to a dictionary')
for keys in dictionary.keys():
    if keys == a_given_key:
        print(f'{a_given_key} is already exist in a dictionary keys')