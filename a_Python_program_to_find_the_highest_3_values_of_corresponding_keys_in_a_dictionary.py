'''
# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
'''

data = {'a': 10, 'b': 25, 'c': 15, 'd': 40, 'e': 30}
maxx = list(data.values())
maxx.sort(reverse=True)
maxx = maxx[:3]
print('Highest 3 values and their corresponding keys:')
for i in maxx:
    for key, value in data.items():
        if value == i:
            print(f'Key: {key}, Value: {value}')
        else: continue