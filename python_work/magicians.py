def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())


# ~ def make_great(magicians):
	# ~ for index in range(len(magicians)):
		# ~ magicians[index] = "the great " + magicians[index]

def make_great(magicians):
	great_magicians = []
	for magician in magicians:
		great_magicians.append("the great " + magician)
	return great_magicians

magicians = ['alice', 'david', 'carolina']

great_magicians = make_great(magicians)
show_magicians(magicians)
show_magicians(great_magicians)

# ~ for magician in magicians:
	# ~ print(magician.title() + ", that was a great trick!")
	# ~ print("I can't wait to see your next trick, " + magician.title() + ".\n")
# ~ print("Thank you, everyone. That was a great magic show")

