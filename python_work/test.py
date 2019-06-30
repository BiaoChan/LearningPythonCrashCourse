# ~ aliens = []

# ~ for alien_number in range(30):
	# ~ new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	# ~ aliens.append(new_alien)

# ~ for alien in aliens[:3]:
	# ~ if alien['color'] == 'green':
		# ~ alien['color'] = 'yellow'
		# ~ alien['speed'] = 'medium'
		# ~ alien['points'] = 10

# ~ for alien in aliens[:5]:
	# ~ print(alien)
# ~ print("...")

# ~ print("Total number of aliens: " + str(len(aliens)))




# ~ pizza = {
	# ~ 'crust':'thick',
	# ~ 'toppings':['mushrooms', 'extra cheese'],
	# ~ }

# ~ print("You ordered a " + pizza['crust'] + "-crust pizza " + 
	# ~ "with the following toppings:")
# ~ for topping in pizza['toppings']:
	# ~ print("\t" + topping)
	
	
	
	
# ~ favorite_languages = {
	# ~ 'jen':['python', 'ruby'],
	# ~ 'sarah':['c'],
	# ~ 'edward':['ruby', 'go'],
	# ~ 'phil':['python', 'haskell'],
	# ~ }

# ~ for name, languages in favorite_languages.items():
	# ~ if len(languages) == 1:
		# ~ print(name.title() + "'s favorite language is:")
	# ~ else:
		
		# ~ print(name.title() + "'s favorite languages are:")
	# ~ for language in languages:
		# ~ print("\t" + language)
	



# ~ users = {
	# ~ 'aeinstein':{
		# ~ 'first':'albert',
		# ~ 'last':'aeinstein',
		# ~ 'location':'princeton',
		# ~ },
	# ~ 'mcurie':{
		# ~ 'first':'marie',
		# ~ 'last':'curie',
		# ~ 'location':'paris',
		# ~ },
	# ~ }

# ~ for username, user_info in users.items():
	# ~ print("Username: " + username)
	# ~ full_name = user_info['first'] + " " + user_info['last']
	# ~ location = user_info['location']
	# ~ print("\t Fullname: " + full_name.title())
	# ~ print("\t Location: " + location.title())



# ~ message = input("Tell me something, and I will repeat it back to you:")
# ~ print(message)


# ~ name = input("Please input your name:")
# ~ print("Hello, " + name.title() + "!")



# ~ prompt = "If you tell us who you are, we can personalize the message you see."
# ~ prompt += "\nWhat is your first name? "
# ~ firstname = input(prompt)
# ~ print("\nHello, " + firstname.title() + "!")


# ~ height = input("How tall are you, in inches? ")
# ~ height = int(height)

# ~ if height >= 36:
	# ~ print("\nYou're tall enough to ride!")
# ~ else:
	# ~ print("\nYou'll be able to ride when you're a little older.")


# ~ number = input("Enter a number, and I'll tell you if it's even or odd:")
# ~ number = int(number)
# ~ if number % 2 == 0:
	# ~ print("\nThe number " + str(number) + " is even")
# ~ else:
	# ~ print("\nThe number " + str(number) + " is odd")


# ~ current_number = 1
# ~ while current_number <= 5:
	# ~ print(current_number)
	# ~ current_number += 1



# ~ prompt = "\nTell me something, and I will repeat it back to you: "
# ~ prompt += "\nEnter 'quit' to end the program."
# ~ message = ""
# ~ while message != "quit":
	# ~ message = input(prompt)
	# ~ if message != "quit":
		# ~ print(message)


# ~ prompt = "\nTell me something, and I will repeat it back to you: "
# ~ prompt += "\nEnter 'quit' to end the program."
# ~ active = True
# ~ while active:
	# ~ message = input(prompt)
	# ~ if message != "quit":
		# ~ print(message)
	# ~ else:
		# ~ active = False


# ~ prompt = "\nTell me something, and I will repeat it back to you: "
# ~ prompt += "\nEnter 'quit' to end the program."
# ~ while True:
	# ~ message = input(prompt)
	# ~ if message != "quit":
		# ~ print(message)
	# ~ else:
		# ~ break

# ~ current_number = 0
# ~ while current_number < 10:
	# ~ current_number += 1
	# ~ if current_number % 2 == 0:
		# ~ continue
	# ~ print(current_number)

x = 1
while x < 5:
	print(x)
	# ~ x += 1


























































