def power(base, exponent):
	result = base ** exponent
	print("{} to the power of {} is {}.".format(base, exponent, result))

def power_return(base, exponent):
	return base ** exponent
#The term doubler is wrong, it multiplies with itself but follow assignment.
def doubler(number):
	return power_return(number, 2)

print("3 multiplied by itself is {}".format(doubler(3)))
print("5 multiplied by itself is {}".format(doubler(5)))


#power(2, 3)
#power(4, 4)
#power(10, 3)

#print("The power of 2 to 8 is {}".format(power_return(2, 8)))
