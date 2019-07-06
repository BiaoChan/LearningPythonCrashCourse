from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")

# favorite_languages = {
# 	'jen':'python',
# 	'sarah':'c',
# 	'edward':'ruby',
# 	'phil':'python',
# 	}
#
# investigators = ['jen', 'zhao', 'phil', 'sarah', 'wang']
#
# for investigator in investigators:
# 	if investigator in favorite_languages.keys():
# 		print("Thank you for your participation in our survey, " +
# 			investigator.title())
# 	else:
# 		print("May I ask if you can take part in our survey, "+
# 			investigator.title() + "?")
