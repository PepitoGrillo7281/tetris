from board import Board

class Game(object):
    def __init__(self):
        # Starts a new game
        self.board = Board((10,20))
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