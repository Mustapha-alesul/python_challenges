'''
# Write a Python program to count the elements in a list until an element is a tuple.
'''

mixed_list = [1, "apple", (2, 3), "banana", (4, 5), 6.5, {"name": "Alice", "age": 25}]
count = 0
for item in mixed_list:
    if isinstance(item,tuple):
        break
    count += 1
print(count)