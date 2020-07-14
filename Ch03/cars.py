cars = ['bmw', 'audi', 'toyota', 'subaru']

# permanently sorts the list alphabetically
cars.sort()
print(cars)

# permanently sorts the list reverse alphabetically
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

# Temporarily sorts the list alphabetically
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# reverse the order of the list permanently
cars.reverse()
print(cars)

# find the length of a list
print(len(cars))