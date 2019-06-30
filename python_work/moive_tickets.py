while True:
	age = input("How old are you? ")
	if age == "":
		break
	age = int(age)
	if age <= 0:
		break
	elif age <= 3:
		print("Watch moive for free")
	elif age <= 12:
		print("You have to pay 10 dollers for the movie")
	else:
		print("You have to pay 15 dollers for the movie")
