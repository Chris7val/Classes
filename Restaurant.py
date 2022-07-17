class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.cuisine_type = cuisine_type
        self.restaurant_name = restaurant_name
        self.number_served = 0

    def set_number_served(self, number_served):
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}")

    def increment_number_served(self, num_served):
        self.number_served += num_served

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_list_of_flavors(self):
        print("The list of flavors are:")
        for flavors in self.flavors:
            print(f"-{flavors}")