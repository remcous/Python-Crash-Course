# Import specific classes from a module
from car import Car
from electric_car import ElectricCar

# Import all classes from a module, dot notation required
# import car
# import electric_car

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2012)
print(my_tesla.get_descriptive_name())