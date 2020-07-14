#initialize an empty list to hold squared numbers
squares = []

for value in range(1,11):
	# ** acts as exponent operator in python
	square = value**2
	# appends the square into the list of squares
	squares.append(square)

print(squares)

# more concise approach
squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

# List Comprehension method to initialize list
squares = [value**2 for value in range(1,11)]
print(squares)