#Battleship Attempt 2

#Imports
import random as rand
import os
import copy as c
from sys import float_repr_style



"""
Defining the Game class to make it easier to 
understand the code further in the project
"""
class Game(object):
    def __init__(self, players):
        self.guesses = 5
        self.player_list = []
        for player in range(players):
                self.player_list.append(self.guesses)
        self.current_player = 1
        self.board = self.create_matrix(5, 5)
        self.board_visible = c.deepcopy(self.board)
        self.ship_row = rand.randint(0, 4)
        self.ship_col = rand.randint(0, 4)
        self.guess_row = 0
        self.guess_col = 0
    
    """
    Defining the many methods that makes the game work,
    starting with the create_matrix where we take in the 
    boards max x and max y to define its size.
    """

    def create_matrix(self, max_x, max_y):
        matrix = list(range(max_x))
        for x in matrix:
            matrix[x] = list(range(max_y))
            for y in range(max_y):
                matrix[x][y] = "O"
        return c.deepcopy(matrix)

    """
    Defining the print_board function, here I respresent
    x as rows
    y as colums
    """

    def print_board(self, board_in):
        x = 0
        y = 0
        for column in board_in:
            y = 0
            for row in column:
                if y == 0:
                    print(" ",row, end=" ")
                elif y == len(board_in[x]):
                    print("", row, end="")
                else:
                    print(row, end=" ")
                y += 1
            print()
            x += 1
        return None

    """
    To avoid repeating the same code twice, I made the user_input method more generalized
    and made a seperate method to take care of if its row or column thats being inputed.
    That way I can make a robust input check without having to repeat code.
    I also use recursive methods here to avoid using while loops.
    """

    def user_input(self):
        line = input("\n")
        if len(line) != 0:
            if int(line) > len(self.board):
                print("That's not even in the ocean! Try again.", end="")
                return self.user_input()
            else:
                return int(line)
        else:
            print("You didn't type anything! Try again", end="")
            return self.user_input()

    """
    I wanted to avoid retyping code as much as possible
    so I did the above function and then created player_guesses
    to take user input and sort it into guesses for row and column
    As of writing this comment I'm avoiding writing any game logic in the function.
    """

    def player_guesses(self):
        if self.player_list[self.current_player-1] == 0:
            return False
        else:
            print("Player {} has {} guesses left.".format(self.current_player, self.player_list[self.current_player-1]))
            
            print("Player {}: Guess row: ".format(self.current_player), end="")
            self.guess_row = self.user_input()
            print("Player {}: Guess column: ".format(self.current_player), end="")
            self.guess_col = self.user_input()

            if self.board[self.guess_row-1][self.guess_col-1] == "X":
                print("You've already guessed on that row! Try again.")
                return self.player_guesses()
            else:
                return None


    """
    Seperating out the game_logic to try to make the main function as readable as possible.
    This is also an exercise to practice writing recursive code instead of using while loops.
    """

    def game_logic(self):
        self.player_guesses()
        if self.board[self.guess_row-1][self.guess_col-1] == self.board[self.ship_row][self.ship_col]: 
            return True
        else:
            if self.player_list[self.current_player-1] > 0:
                print("Sorry, you missed!")
                self.board[self.guess_row-1][self.guess_col-1] = "X"
                self.board_visible[self.guess_row-1][self.guess_col-1] = "X"
                self.player_list[self.current_player-1] -= 1
                self.print_board(self.board_visible)

                return self.game_logic()
            else:
                print("Player {} has run out of guesses.".format(self.current_player))
                return False

    def main(self):
        os.system("clear")
        self.print_board(self.board)
        print(self.ship_row, self.ship_col)
        self.board[self.ship_row][self.ship_col] = "S"
        if self.game_logic() == True:
            self.print_board(self.board)
            print("Congratulations! Player {} won the game!".format(self.current_player))
        else:
            print("Game over! Player {} has lost!".format(self.current_player))




battleship = Game(1)
battleship.main()