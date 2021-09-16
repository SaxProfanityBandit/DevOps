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
        #Stuff here
    def __init__(self, players):
        self.guesses = 5
        self.player_list = []
        for player in range(players):
                self.player_list.append(self.guesses)
        self.players = 1
        self.board = self.create_matrix(5, 5)
        self.ship_row = 1
        self.ship_col = 1
    
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
        for row in self.board:
            y = 0
            for column in row:
                if y == 0:
                    print(" ",column, end=" ")
                elif y == len(self.board[x]):
                    print("", column, end="")
                else:
                    print(column, end=" ")
                y += 1
            print()
            x += 1
        return None


battleship = Game(1)
battleship.print_board()