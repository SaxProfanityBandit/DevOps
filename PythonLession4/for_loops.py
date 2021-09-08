#Is actually not a list. Learned that.
def check_even():
	numbers = range(0, 100)
	for number in numbers:
		if number % 2 == 0:
			print("{} is even.".format(number))
		else:
			print("{} is not even.".format(number))

def almost_total(numbers):
	sum_of_list = []
	for i in range(1, len(numbers)-1):
		sum_of_list.append(numbers[i])
		print(numbers[i])
	return sum(sum_of_list)
	#Doing this way to practice/show the sum function.

print(almost_total([1, 2, 4, 5]))		
