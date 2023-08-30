'''
#  Write a Python program to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
'''

Sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
a, b, c = Sample_data
g,k,l = list(a.values()), list(b.values()), list(c.values())
h, m, n={}, {}, {}
h[g[0]], m[k[0]], n[l[0]] = g[1], k[1], l[1]
Counter = {key: h.get(key,0) + m.get(key,0) + n.get(key,0) for key in set(h) | set(m) | set(n)}
print(f'Counter({Counter})')