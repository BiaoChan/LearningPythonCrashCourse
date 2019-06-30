dream_places = {}

investigate_active = True

while investigate_active:
	name = input("What's your name?")
	place = input("If you could visit one place in the world, where would you go? ")
	
	dream_places[name] = place
	
	repeat = input("Would you like to ask another person?(Y/N)")
	if repeat == 'N':
		investigate_active = False

print("\n--- Results ---")
for name, dream_place in dream_places.items():
	print(name.title() + "'s dream place is " + dream_place.title())
