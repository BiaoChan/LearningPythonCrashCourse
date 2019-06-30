sandwich_orders = ['tuna', 'pastrami', 'bacon', 'pastrami', 'cheese', 'pastrami', 'beef']
finished_sandwiches = []

print("All pastrami sandwich has been sold")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop(0)
	print("I made your " + current_sandwich + " sandwich.")
	finished_sandwiches.append(current_sandwich)

print("All these sandwiches are ready: ")
for sandwich in finished_sandwiches:
	print("\t" + sandwich)
