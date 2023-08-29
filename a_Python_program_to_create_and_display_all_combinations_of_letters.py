'''
# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
'''

Sample_data = {'1':['a','b'], '2':['c','d']}
a, b =list(Sample_data.values())
for letter in a:
    for lett in b:
        c = letter +lett
        print(c)