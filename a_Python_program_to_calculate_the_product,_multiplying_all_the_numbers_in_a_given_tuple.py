'''
# Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648
'''

Original_Tuple = (4, 3, 2, 2, -1, 18)
Original_Tuple1 = (2, 4, 8, 8, 3, 2, 9)

def productt(Tupplee):
    Product = 1
    for item in Tupplee:
        Product *= item
    return Product
result = productt(Original_Tuple)
print(f'Product of all elements of tuple{Original_Tuple} is : {result}')
result1 = productt(Original_Tuple1)
print(f'Product of all elements of tuple{Original_Tuple1} is : {result1}')
