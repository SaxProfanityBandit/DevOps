#Imports
import os
import random as ran
import copy as c
#Functions

def create_matrix(max_x, max_y):
	matrix = list(range(max_x))
	for x in matrix:
		matrix[x] = list(range(max_y))
		for y in range(max_y):
			matrix[x][y] = "O"
	return matrix

def print_board(board_in):
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
	board = create_matrix(15, 15)
	print_board(board)
	ship_row = random_row(board)
	ship_col = random_col(board[ship_row])
	
	#Creating a copy of the board to show the player without revealing the ship.
	board_copy = c.deepcopy(board)
	#Marking the ship tile.
	board[ship_row][ship_col] = "S"


	#Defining players
	player_list = list()
	guesses = 5
	for player in range(players):
		player_list.append(guesses)
	player = 1
	#User input and game logic
	while player-1 < len(player_list):
		while player_list[player-1] > 0:
			guess_row = input("Player {}: Guess row: ".format(player))
			guess_column = input("Player {}: Guess column: ".format(player))
			
			#Sanity checking
			while len(guess_row) == 0:
				print("Player {}: You didn't enter a number in the row guess!".format(player))
				guess_row = input("Player {}: Guess row: ".format(player))
			while len(guess_column) == 0:
				print("Player {}: You didn't enter a number in the column guess!".format(player))
				guess_column = input("Player {}: Guess column: ".format(player))
			guess_row = int(guess_row) - 1
			guess_column = int(guess_column) - 1
			
			#Checking if they are outside the board/list indexes.
			while guess_row > len(board)-1 or guess_row+1 <= 0:
				print("Player {}: Outside of bounds, try again!".format(player))	
				guess_row = int(input("Guess row: ")) - 1
			while guess_column > len(board[guess_row])-1 or guess_column+1 <= 0:
				print("Player {}: Outside of bounds, try again!".format(player))
				guess_column = int(input("Guess column: ")) - 1
			#If they guess correctly they win.
			if board[guess_row][guess_column] == "S":
				print("Player {}: Congratulations, you sank the ship!".format(player))
				print_board(board)
				return True
			else:
				player_list[player-1] -= 1
				if board[guess_row][guess_column] == "X":
					print("You've already guessed that!")
				else:
					board[guess_row][guess_column] = "X"
					board_copy[guess_row][guess_column] = "X"
					print_board(board_copy)
				print("Player {}: Sorry, you missed! Try again! You have {} guesses left.".format(player, player_list[player-1]))
			if player >= len(player_list):
				player = 1
			else:
				player += 1
		if player_list[player-1] == 0:
			print("Player {}: Game over! No more guesses".format(player))
			print_board(board)
			return False
		player = 1

#Creating a game session.
players = input("How many players? ")
while len(players) == 0:
	print("You didn't input a number of players. Try again")
	players = input("How many players? ")
	
game(int(players))
