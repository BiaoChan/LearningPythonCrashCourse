def make_sandwich(*ingredients):
	print("\nMaking a sandwich with following ingredients:")
	for ingredient in ingredients:
		print("- " + ingredient)

make_sandwich('eggs', 'bacon', 'beef')
