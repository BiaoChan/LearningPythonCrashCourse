pizza_toppings = []

print("Please order pizza with toppings, enter 'quit' to quit")

while True:
	pizza_topping = input()
	if pizza_topping != 'quit':
		print("We'll add " + pizza_topping + " in pizza.")
	else:
		break
		
