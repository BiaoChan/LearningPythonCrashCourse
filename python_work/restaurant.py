class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This is a " + self.cuisine_type + " restaurant named " +
            self.restaurant_name.title())

    def open_restaurant(self):
        print("The restaurant is open now!")

    def get_number_served(self):
        print("There are " + str(self.number_served) +
            " peoples have been served in this restaurant.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
