#Is actually not a list. Learned that.
numbers = range(0, 100)
for number in numbers:
	if number % 2 == 0:
		print("{} is even.".format(number))
	else:
		print("{} is not even.".format(number))


