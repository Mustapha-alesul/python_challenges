'''
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''

dictionary = {}
n_value = int(input('Enter a last number to generate a dictionary'))
for value in range (n_value+1):
    dictionary[value] = value ** 2
print(dictionary)