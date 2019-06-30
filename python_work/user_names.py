current_users = ['admin', 'zhao', 'qian', 'sun', 'li']
new_users = ['Admin', 'John', 'Chen', 'Qian', 'li']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("The username has been used, plz try another username.")
	else:
		print("Congratulations, the username haven't been used")
