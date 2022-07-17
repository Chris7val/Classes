# from Restaurant import Restaurant, IceCreamStand
# flavor_list = ['strawberry', 'chocolate', 'vanilla', 'banana']
# ice_cream_stand0 = IceCreamStand('mario', 'ice cream', flavor_list)
# ice_cream_stand0.get_list_of_flavors()
# ice_cream_stand0.describe_restaurant()
#
# restaurant0 = Restaurant('Olive Garden', 'Italian Food')
# restaurant1 = Restaurant('Red Lobster', 'Sea Food')
# restaurant2 = Restaurant('Wendys', 'Fast Food')
# restaurant0.describe_restaurant()
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# # restaurant0.open_restaurant()
# restaurant0.set_number_served(15)
# restaurant0.increment_number_served(10)
# print(restaurant0.number_served)

# class User:
#     def __init__(self, first_name, last_name, favorite_color, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.favorite_color = favorite_color
#         self.age = age
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f"\nUser summary\n____________\nFirst name:{self.first_name}"
#               f"\nLast name:{self.last_name}\nFavorite color:{self.favorite_color}"
#               f"\nAge:{self.age}")
#
#     def increment_login_attempts(self):
#         self.login_attempts = self.login_attempts + 1
#         return self.login_attempts
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#     def greet_user(self):
#         print(f"\nHello {self.first_name} {self.last_name}")
#
#
# user0 = User('Christopher', 'Valdez', 'blue', 21)
# # user1 = User('Ashley', 'Valdez', 'blue', 21)
# # user2 = User('Chelsy', 'Valdez', 'blue', 21)
# # user0.describe_user()
# # user1.describe_user()
# # user2.describe_user()
# # user0.greet_user()
# # user1.greet_user()
# # user2.greet_user()
# # user0.increment_login_attempts()
# # user0.increment_login_attempts()
# # user0.increment_login_attempts()
# # user0.increment_login_attempts()
# # user0.increment_login_attempts()
# # user0.increment_login_attempts()
# # print(user0.login_attempts)
# # user0.reset_login_attempts()
# # print(user0.login_attempts)
#
#
# class Admin(User):
#
#     def __init__(self, first_name, last_name, favorite_color, age, privileges):
#         super().__init__(first_name, last_name, favorite_color, age)
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print("List of privileges are:")
#         for privilege in self.privileges:
#             print(f"-{privilege}")
#
#
# list_of_privileges = ['can add post', 'can delete post', 'can ban user']
# admin = Admin('christopher', 'valdez', 'blue', 21, list_of_privileges)
# admin.show_privileges()
