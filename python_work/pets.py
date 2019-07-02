# ~ pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ~ print(pets)

# ~ while 'cat' in pets:
	# ~ pets.remove('cat')

# ~ print(pets)


def describe_pet(pet_name = 'xixi', animal_type = 'dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name + ".")


# ~ describe_pet('dog', 'dawei')
# ~ describe_pet('cat', 'xixi')

describe_pet(animal_type = 'dog', pet_name = 'haha')

describe_pet(pet_name = 'xixi', animal_type = 'cat')

describe_pet('white')

describe_pet()
