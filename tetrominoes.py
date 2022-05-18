"""
All the "place" functions place a tetrominoe
in the first 4 rows of the board. First we check if the
pixels are empty. If not, the game ends (we return False). 


All available tetrominoes in the original game can be found
here: https://tetris.fandom.com/wiki/Tetromino
"""
from board import Board
import random
from pprint import pprint

class Tetrominoes(object):
    def __init__(self,board):
        self.available={
            'I':self.place_i,
            'J':self.place_j,
            'L':self.place_l,
            'O':self.place_o,
            'S':self.place_s,
            'T':self.place_t,
            'Z':self.place_z,
        }
        self.board=board

    def place_random(self):
        """
        Adds a random 
        """
        selection = random.choice(list(self.available.keys()))
        self.available[selection]()
        return selection

    def check_available(self):
        """
        Checks if the 4x2 pixels at the top of the
        board are available.

        :param list board: Current board of the game.
        :return bool: if all of them are empty.
        """
        cond1=self.board.board[0][int(self.board.dimensions[0]/2)]==0
        cond2=self.board.board[1][int(self.board.dimensions[0]/2)]==0
        cond3=self.board.board[0][int(self.board.dimensions[0]/2)+1]==0
        cond4=self.board.board[1][int(self.board.dimensions[0]/2)+1]==0
        cond5=self.board.board[0][int(self.board.dimensions[0]/2)+2]==0
        cond6=self.board.board[1][int(self.board.dimensions[0]/2)+2]==0
        cond7=self.board.board[0][int(self.board.dimensions[0]/2)+3]==0
        cond8=self.board.board[1][int(self.board.dimensions[0]/2)+3]==0
        return cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8

    def place_i(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[0][int(self.board.dimensions[0]/2)]=2
            self.board.board[0][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[0][int(self.board.dimensions[0]/2)+2]=2
            self.board.board[0][int(self.board.dimensions[0]/2)+3]=2  
            return True
        return False
    def place_j(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[0][int(self.board.dimensions[0]/2)]=2
            self.board.board[1][int(self.board.dimensions[0]/2)]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+2]=2  
            return True
        return False
    def place_l(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[0][int(self.board.dimensions[0]/2)+2]=2
            self.board.board[1][int(self.board.dimensions[0]/2)]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+2]=2  
            return True
        return False
    def place_o(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[0][int(self.board.dimensions[0]/2)]=2
            self.board.board[0][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+1]=2  
            return True
        return False
    def place_s(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[1][int(self.board.dimensions[0]/2)]=2
            self.board.board[0][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[0][int(self.board.dimensions[0]/2)+2]=2  
            return True
        return False
    def place_t(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[0][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+2]=2  
            return True
        return False
    def place_z(self):
        """
        :param list board: Current board of the game.
        :return bool: If the game can continue.
        """
        if self.check_available():
            self.board.board[0][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[0][int(self.board.dimensions[0]/2)]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+1]=2
            self.board.board[1][int(self.board.dimensions[0]/2)+2]=2  
            return True
        return False