# favorite_number = {
# 	'chen':97,
# 	'zhao':91,
# 	'sun':21,
# 	'li':321,
# 	'wang':321,
# 	}
#
# print(set(favorite_number.values()))
#
#
# for number in set(favorite_number.values()):
# 	print(number)


import json

def get_new_number():
	favorite_number = input("What's your favorite number? ")
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)
	return favorite_number

def get_stored_number():
	filename = 'favorite_number.json'
	try:
		with open(filename, 'r') as f_obj:
			favorite_number = json.load(f_obj)
	except FileNotFoundError:
		favorite_number = None
	return favorite_number

def greet():
	favorite_number = get_stored_number()
	if favorite_number:
		flag = input("I know your favorite number, it's " + str(favorite_number)
		+ ", right?(Y/N)")
	else:
		flag = 'N'

	if flag == 'N':
		favorite_number = get_new_number()
		print("I know your favorite number, it's " + str(favorite_number)
			+ ".")
	else:
		print("Bye~")


greet()
