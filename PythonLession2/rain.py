#Regn uppgift.
rain = input("Is it raining? y/n? ").lower()
clothes = input("Do you got rain clothes? y/n? ").lower()
allergy = input("Do you have any sun allergy? y/n? ").lower()

#Input checking
if rain == 'y' or rain == 'n':
	if clothes == 'y' or clothes == 'n':
		if allergy == 'y' or allergy == 'n':
			if rain == 'y':
				if clothes == 'y':
					if allergy == 'y':
						print("Go outside with rain clothes.")
					else:		
						print("Go outside with rain clothes.")
				else:
					print("Don't go outside, it's raining.")
			else:
				if allergy == 'y':
					print("Go outside, apply sunscreen cream.")
				else:
					print("Just go outside, its nice!")
		else:
			print("Input error, please only answer with y or n")
	else:
		print("Input error, please only answer with y or n")
else:
	print("Input error, please only answer with y or n")
