def power(base, exponent):
	result = base ** exponent
	print("{} to the power of {} is {}.".format(base, exponent, result))

def power_return(base, exponent):
	return base ** exponent

power(2, 3)
power(4, 4)
power(10, 3)

print("The power of 2 to 8 is {}".format(power_return(2, 8)))
