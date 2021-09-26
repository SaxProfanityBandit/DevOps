animals = ['German Shepard', 'Russian Blue', 'Tiger Shark', 'Black Adder']
#print(animals)

animals[0] = 'Capybara'
animals[3] = 'Trapdoor Spider'
#print(animals)

numbers = [2, 4, 6]
#print(numbers[1])

numbers[1] *= 5
#print(numbers)

#print(numbers[1:])
numbers.pop(1)
numbers.remove(6)
#print(numbers)

def find_strings(x)
	count = 0
	for word in x:
		try:
			if word == "fizz":
				count += 1
		except:
			print("You tried comparing something that is not a string!")
			continue
	return count

x = [23424123, 54563, 1234, "fizz", 31412, "test"]

print(find_strings(x))
print(find_strings([134, "fizz", "bar", "foo", "fizz", "hoppsan"]))

def loop_through_string(line):
	for letter in line:
		print(letter)


loop_through_string("Linux och skriptspråk")
