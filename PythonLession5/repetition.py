def digit_sum(numbers):
	res = 0
	for digit in str(numbers):
		res += int(digit)
	return res

print(digit_sum(1234))

def factorial(number):
	x = number
	fact = 0
	while x > 0:
		x -= 1
		fact += number * x
	return fact

print(factorial(4))

def is_prime(n):
	if n > 1:
		for i in range(2, n):
			if n % i == 0:
				return False
	return True

print(is_prime(18))

def reverse(line):
	i = len(line)
	line_reverse = ""
	while i > 0:
		line_reverse += line[i-1]
		i -= 1
	return line_reverse

print(reverse("Linux"))

def anti_vowel(line):
	new_line = line
	vowels = ['a','e','i','o','u','å','ä','ö']
	for x in line.lower():
		for vowel in vowels:
			if x == vowel:
				new_line = new_line.replace(x, "")
	return new_line

print(anti_vowel("Hejsan"))		

def scrabble_score(line):
	points = 0
	score = {
		"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
 		"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
 		"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
 		"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
		"x": 8, "z": 10
	}
	
	for character in line:
		for key in score:
			if character.lower() == key:
				points += score[key]
	return points

print(scrabble_score("Helix"))

def censor(text, word):
	return text.replace(word, "*")

print(censor("fan också! fan också! fan också!", "fan"))


def count(sequence, item):
	amount = 0
	for x in sequence:
		if x == item:
			amount += 1
	return amount

print(count([1,2,2,2,5],2))

def purify(numbers):
	for number in numbers:
		if number % 2 > 0:
			numbers.remove(number)
	return numbers

print(purify([1,2,3,4,5]))


def remove_duplicates(list_in):
	list_out = []
	for item in list_in:
		if item not in list_out:
			list_out.append(item)
	return list_out

print(remove_duplicates([1,2,1,2,3,4,5]))

def sum_numbers(number):
	sum = 0
	while(numbers > 0):
		
