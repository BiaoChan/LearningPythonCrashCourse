# def build_profile(first, last, **user_info):
# 	"""create a dictionary, include everything we know about user"""
# 	profile = {}
# 	profile['first_name'] = first
# 	profile['last_name'] = last
# 	for key, value in user_info.items():
# 		profile[key] = value
# 	return profile
#
# user_profile = build_profile('albert', 'einstein',
# 	location = 'princeton', field = 'physics')
#
# print(user_profile)
#
# my_profile = build_profile('albert', 'einstein', weight = 100, height = 180,
# 	looking = 'very handsome')
#
# print(my_profile)

class User_profile():
	def __init__(self, first_name, last_name, **user_info):
		self.profile = {}
		self.profile['first_name'] = first_name
		self.profile['last_name'] = last_name
		for key, value in user_info.items():
			self.profile[key] = value

	def describe_user(self):
		print("User's profiles:")
		for key, value in self.profile.items():
			print(key + ": " + value)

	def greet_user(self):
		full_name = self.profile['first_name'] + " " + self.profile['last_name']
		print("Hello, " + full_name.title() + "!")


my_profile = User_profile('wang', 'sicong', money='100', outlooking='handsome')
my_profile.describe_user()
