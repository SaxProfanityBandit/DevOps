#Battleship Attempt 2

#Imports
import random as rand
import os
import copy as c



"""
Defining the Game class to make it easier to 
understand the code further in the project
"""
class Game(object):
    guess_row = 1
    guess_col = 1

    def __init__(self, players):
        self.guesses = 5
        self.player_list = []
        for player in range(players):
                self.player_list.append(self.guesses)
        self.current_player = 1
        self.board = self.create_matrix(5, 5)
        self.ship_row = rand.randint(0, 4)
        self.ship_col = rand.randint(0, 4)
    
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

    def print_board(self):
        x = 0
        y = 0
        for column in self.board:
            y = 0
            for row in column:
                if y == 0:
                    print(" ",row, end=" ")
                elif y == len(self.board[x]):
                    print("", row, end="")
                else:
                    print(row, end=" ")
                y += 1
            print()
            x += 1
        return None

    """def user_input(self):
        print("Player {}: Guess row: ".format(self.current_player))
        guess_row = input("\n")
        if len(guess_row) != 0:
            if int(guess_row) > len(self.board):
                print("That's not even in the ocean! Try again.")
                return self.user_input()
            else:
                self.guess_row = int(guess_row)
        else:
            print("You didn't type anything. Try again!")
            return self.user_input()

        print("Player {}: Guess column: ".format(self.current_player))
        guess_col = input("\n")
        if len(guess_col) != 0:
            if int(guess_col) > len(self.board[int(guess_row)]):
                print("That's not even in the ocean! Try again.")
                return self.user_input()
            else:
                self.guess_col = int(guess_col)
        else:
            print("You didn't type anything. Try again!")
            return self.user_input()
        """
            




    def main(self):
        os.system("clear")





battleship = Game(1)
battleship.print_board()
battleship.user_input()