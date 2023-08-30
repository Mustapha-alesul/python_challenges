'''
# Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''

Sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Output = []
for tuples in Sample_data:
    if tuples == ():
        continue
    else:
        Output.append(tuples)
print(Output)