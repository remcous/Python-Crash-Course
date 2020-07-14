cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking condition is case sensitive
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')