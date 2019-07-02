def greet_users(users):
	for user in users:
		print("Hello, " + user.title() + "!")

users = ['zhaocongcong', 'chenbiao', 'sun', 'li']

greet_users(users)
