'''
# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
'''

Sample_dictionary = {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
s = list(Sample_dictionary)
a, b = s
c = set(a.items())
d = set(b.items())
e = c.intersection(d)
e = dict(e)
for key, value in e.items():
    print(f'{key}: {value} is present in both x and y')