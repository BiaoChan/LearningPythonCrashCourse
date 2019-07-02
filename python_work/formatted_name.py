def get_formatted_name(first_name, last_name, middle_name = ''):
	"""return name"""
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('chen', 'biao')
print(musician)

musician = get_formatted_name('chen', 'biao', 'shuai')
print(musician)
