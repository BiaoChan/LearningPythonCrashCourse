favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

investigators = ['jen', 'zhao', 'phil', 'sarah', 'wang']

for investigator in investigators:
	if investigator in favorite_languages.keys():
		print("Thank you for your participation in our survey, " + 
			investigator.title())
	else:
		print("May I ask if you can take part in our survey, "+ 
			investigator.title() + "?")
