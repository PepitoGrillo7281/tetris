from board import Board
from tetrominoes import Tetrominoes
import pygame
import sys
import time
import random

class Game(object):
    def __init__(self,screen):
        # Starts a new game
        self.board = Board((10,22))
        self.tetrominoes = Tetrominoes(self.board)
        self.screen=screen
        self.colors ={
            # 0:(0,0,0) # avoided to improve rendering
            1:(100,100,100),
            2:(255,0,0),
            3:(150,150,150),
        }
        self.pixel_size = 22
        self.blit_rate = 0.5 # time in seconds between each blit. Can be a float
        self.last_blit = time.time()
        self.blitting=False
        
    def paint_board(self):
        self.screen.fill((0, 0, 0))
        y=0
        for row in self.board.board:
            x=0
            for element in row:
                x_start = x*self.pixel_size+self.pixel_size
                y_start = y*self.pixel_size+self.pixel_size
                x_end = self.pixel_size
                y_end =self.pixel_size
                pygame.draw.rect(self.screen,(20,20,20),pygame.Rect(x_start,y_start,x_end,y_end),2)
                if element!=0:   
                    pygame.draw.rect(self.screen,self.colors[element],pygame.Rect(x_start,y_start,x_end,y_end))
                x+=1
            y+=1

    def blit(self):
        self.blitting=True
        self.last_blit = time.time()
        state = self.board.blit()
        if state:
            cont=self.tetrominoes.place_random()
            if not cont:
                pass #GAME MUST END!
        self.paint_board()
        pygame.display.flip()
        self.blitting=False

    def run(self):
        if (time.time()-self.last_blit)>self.blit_rate:
            print(self.blit_rate)
            if self.blit_rate>0.15:
                self.blit_rate-=(self.blit_rate/100)*1.002*random.randint(10,12)/10
            elif self.blit_rate>0.1:
                self.blit_rate-=(self.blit_rate/100)*1.0005*random.randint(10,11)/10
            self.blit()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not self.blitting:
                    if event.key == pygame.K_LEFT:
                        self.board.move_left()
                        self.paint_board()
                    if event.key == pygame.K_RIGHT:
                        self.board.move_right()
                        self.paint_board()
                    if event.key == pygame.K_DOWN:
                        self.blit()
                    if event.key == pygame.K_UP:
                        self.board.rotate()
                        self.paint_board()
            pygame.display.flip()

if __name__=='__main__':
    g = Game(pygame.display.set_mode([800, 550]))
    g.blit()
    g.tetrominoes.place_random()
    while True:
        g.run()