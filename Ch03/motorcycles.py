motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# appends element to the end of the list
motorcycles.append('ducati')
print(motorcycles)

# deletes a element in the list
del motorcycles[1]
print(motorcycles)

# inserts an element at a specific index in the list
motorcycles.insert(1, 'yamaha')
print(motorcycles)

# uses the pop() method to remove the last element of the list and return the element
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# can pop() from a specific index
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

# remove by value
motorcycles.remove('suzuki')
print(motorcycles)