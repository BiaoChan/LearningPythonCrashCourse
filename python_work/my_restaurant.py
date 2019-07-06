from restaurant import Restaurant

my_restaurant = Restaurant('shaxian', 'china_food')

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
#
# # restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# restaurant1 = Restaurant('lanzhoulamian', 'green')
# restaurant2 = Restaurant('chongqingxiaomian', 'chuan')
# restaurant3 = Restaurant('jinju', 'hang')
#
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()


my_restaurant.get_number_served()

my_restaurant.set_number_served(12)
my_restaurant.get_number_served()

my_restaurant.increment_number_served(21)
my_restaurant.get_number_served()
