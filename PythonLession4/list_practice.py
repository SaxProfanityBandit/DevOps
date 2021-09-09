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

def find_strings(x):
	for word in x:
		if word == "fizz":
			count += 1
	return count

#print(find_strings(["fizz", "bar", "foo", "fizz", "hoppsan"]))

def loop_through_string(line):
	i = 0
	for letter in line:
		print(letter)


loop_through_string("Linux och skriptspråk")
