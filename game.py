from board import Board
from tetrominoes import Tetrominoes
import pygame
import sys
import time

class Game(object):
    def __init__(self,screen):
        # Starts a new game
        self.board = Board((10,22))
        self.tetrominoes = Tetrominoes(self.board)
        self.screen=screen
        self.colors ={
            # 0:(0,0,0) # avoided to improve rendering
            1:(200,150,175),
            2:(255,0,0),
        }
        self.pixel_size = 22
        self.blit_rate = 1 # time in seconds between each blit. Can be a float
        self.last_blit = time.time()
        
    def paint_board(self):
        y=0
        for row in self.board.board:
            x=0
            for element in row:
                if element!=0:
                    x_start = x*self.pixel_size+self.pixel_size
                    y_start = y*self.pixel_size+self.pixel_size
                    x_end = self.pixel_size
                    y_end =self.pixel_size
                    pygame.draw.rect(self.screen,self.colors[element],pygame.Rect(x_start,y_start,x_end,y_end),2)
                x+=1
            y+=1

    def blit(self):
        print(time.time()-self.last_blit)
        self.last_blit = time.time()
        self.screen.fill((0, 0, 0))
        state = self.board.blit()
        if state:
            cont=self.tetrominoes.place_random()
            if not cont:
                pass #GAME MUST END!
        self.paint_board()
        pygame.display.flip()

    def run(self):
        if (time.time()-self.last_blit)>self.blit_rate:
            self.blit()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                sys.exit()

if __name__=='__main__':
    g = Game(pygame.display.set_mode([800, 550]))
    g.blit()
    g.tetrominoes.place_random()
    while True:
        g.run()