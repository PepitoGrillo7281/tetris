from board import Board
import time

class Game(object):
    def __init__(self):
        # Starts a new game
        self.board = Board((5,10))
        self.board.board[0][int(self.board.dimensions[0]/2)]=2

    def blit(self):
        state = self.board.blit()
        if state:
            self.board.board[0][int(self.board.dimensions[0]/2)]=2
        self.board.print_board()
        x=input()

g = Game()
while True:
    g.blit()