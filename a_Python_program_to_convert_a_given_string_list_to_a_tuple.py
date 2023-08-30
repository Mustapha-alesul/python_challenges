'''
# Write a Python program to convert a given string list to a tuple.
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# <class 'tuple'>
'''

Original_string = 'python 3.0'
print(Original_string)
print(type(Original_string))
Original_string = Original_string.replace(' ','')
Converted_string = tuple(Original_string)
print(Converted_string)
print(type(Converted_string))