from random import randint

random_number = randint(1, 10)
guesses_left = 3

while guesses_left != 0:
	print("You have {} guesses left.".format(guesses_left))
	guess = input("Guess a number between 1-10: ")
	while guess == "":
		print("You didn't write a number, try again")
		guess = input("Guess a number between 1-10: ")
	guess = int(guess)
	if guess == random_number:
		print("You won!")
		break
	guesses_left -= 1
else:
	print("You ran out of guesses, game over!")
