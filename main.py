"""
Starts the game and displays the main menu (not yet)
"""

import pygame
from game import Game

class Tetris(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([800, 550])
        self.font_subtitle = pygame.font.Font('sources/arcade.ttf',52)
        self.font_plain_text = pygame.font.Font('sources/arcade.ttf',22)

    def start_game(self):
        g = Game(self)
        g.blit()
        g.tetrominoes.place_random()
        while True:
            g.run()

if __name__=='__main__':
    t = Tetris()
    t.start_game()