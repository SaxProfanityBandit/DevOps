#Imports
import os
import random as ran

#Constants


#Functions

def create_matrix(max_x, max_y):
	matrix = list(range(max_x))
	for x in matrix:
		matrix[x] = list(range(max_y))
		for y in range(max_y):
			matrix[x][y] = "O"
	return matrix

def print_board(board_in):
	#os.system("clear")
	i = 0
	j = 0
	for x in board_in:
		j = 0
		print("".rjust(int(os.get_terminal_size().columns/3), "~"), end="")
		for y in x:
			if j == 0:
				print(" {}".format(y), end=" ")
			elif j == len(board_in[i])-1:
				print("{} ".format(y), end="")
			else:
				print(y, end=" ")
			j += 1	
		print("".ljust(int(os.get_terminal_size().columns/3), "~"), end="")
		print()
		i += 1
	return None


#print_board(create_matrix(5, 5))


#Why are these needed?
def random_row(board_in):
	return ran.randint(0, len(board_in)-1)

def random_col(row_in):
	return ran.randint(0, len(row_in)-1)


#Defining a game session
def game(players):
	#Clearing the screen between every game session.
	os.system("clear")	
	
	#Session variables
	board = create_matrix(5, 5)
	print_board(board)
	ship_row = random_row(board)
	ship_col = random_col(board[ship_row])
	board[ship_row][ship_col] = "S"
	#Debug
	#print_board(board)
	guesses = 5
	
	#User Input
	while guesses > 0:
		guess_row = int(input("Guess row: "))-1
		guess_column = int(input("Guess column: "))-1
	
		if guess_row > len(board):
			print("Outside of bounds, try again!")
		elif guess_column > len(board[guess_row]):
			print("Outside of bounds, try again!")
		elif board[guess_row][guess_column] == "S":
			print("Congratulations, you sank the ship!")
			print_board(board)
			return True
		else:
			guesses -= 1
			if board[guess_row][guess_column] == "X":
				print("You've already guessed that!")
			else:
				board[guess_row][guess_column] = "X"
			print("Sorry, you missed! Try again! You have {} guesses left.".format(guesses))
	if guesses == 0:
		print("Game over! No more guesses")
		print_board(board)
		return False


game(int(input("How many players(1/2)? ")))
