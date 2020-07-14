dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# TypeError: 'tuple' object does not support item assignment
#dimensions[0] = 250

print("\nOriginal Dimensions:")
for dimension in dimensions:
	print(dimension)

# how to change the values in a tuple
dimensions = (400, 100)
print ("\nModified Dimensions:")
for dimension in dimensions:
	print(dimension)