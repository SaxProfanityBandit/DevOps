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
	
	#Defining players
	player_list = list()
	guesses = 5
	for player in range(players):
		player_list.append(guesses)
	print(player_list)
	player = 1
	#User Input
	while player-1 < len(player_list):
		print(player)
		while player_list[player-1] > 0:
			guess_row = input("Player {}: Guess row: ".format(player))
			guess_column = input("Player {}: Guess column: ".format(player))
			
			#Sanity checking
			if len(guess_row) == 0:
				print("You didn't enter a number in the row guess!")
				guess_row = input("Guess row: ")
			elif len(guess_column) == 0:
				print("You didn't enter a number in the column guess!")
				guess_column = input("Guess column: ")
			else:
				print()
			
			guess_row = int(guess_row) - 1
			guess_column = int(guess_column) - 1

			if guess_row > len(board):
				print("Player {}: Outside of bounds, try again!".format(player))
			elif guess_column > len(board[guess_row]):
				print("Player {}: Outside of bounds, try again!".format(player))
			elif board[guess_row][guess_column] == "S":
				print("Player {}: Congratulations, you sank the ship!".format(player))
				print_board(board)
				return True
			else:
				player_list[player] -= 1
				if board[guess_row][guess_column] == "X":
					print("You've already guessed that!")
				else:
					board[guess_row][guess_column] = "X"
				print("Player {}: Sorry, you missed! Try again! You have {} guesses left.".format(player, player_list[player]))
		if player_list[player] == 0:
			print("Player {}: Game over! No more guesses".format(player))
			print_board(board)
			return False
		player += 1


game(int(input("How many players(1/2)? ")))
