def build_person(first_name, last_name, age = ''):
	person = {'first':first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person

muscian = build_person('chen', 'biao')
print(muscian)

muscian = build_person('chen', 'biao', 19)
print(muscian)
