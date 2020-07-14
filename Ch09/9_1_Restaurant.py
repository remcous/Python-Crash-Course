class Restaurant():
    """Class to store information about a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with a name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Outputs the known information about the restaurant."""
        print(self.restaurant_name.title() + " is a " 
            + self.cuisine_type.title() + " Restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")

restaurant1 = Restaurant('manchu wok', 'chinese')
restaurant2 = Restaurant('swiss chalet', 'chicken')
restaurant3 = Restaurant('taco bell', 'mexican')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()