"""
# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

"""

Original_tuple_values = (('333', '33'), ('1416', '55'))
Original_tuple_values = list(Original_tuple_values)
for item in Original_tuple_values:
    item = list(item)

