def shut_down(s):
	if s == 'y' or s == 'n':
		if s == 'y':
			return "Shutting down!"
		else:
			return "Shut down aborted!"
	else:
		return "Sorry. Wrong input."

print(shut_down(input("Are you sure you want to shut down(y/n)? ").lower()))
			
