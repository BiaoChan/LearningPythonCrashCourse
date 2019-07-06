class UserProfile():
	def __init__(self, first_name, last_name, **user_info):
		self.profile = {}
		self.profile['first_name'] = first_name
		self.profile['last_name'] = last_name
		for key, value in user_info.items():
			self.profile[key] = value
		self.login_attempts = 0

	def describe_user(self):
		print("User's profiles:")
		for key, value in self.profile.items():
			print(key + ": " + value)

	def greet_user(self):
		full_name = self.profile['first_name'] + " " + self.profile['last_name']
		print("Hello, " + full_name.title() + "!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0
