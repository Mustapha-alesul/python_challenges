'''
# Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 200, 'b': 200, 'd':400}
d3 = {}
for key, value in d1.items():
    if key in d2:
        d3[key] = value + d2[key]
    else:
        d3[key] = value
for key_2, value_2 in d2.items():
    if key_2 not in d3:
        d3[key_2] = value_2
    else:
        continue
print(f'Counter({d3})')

