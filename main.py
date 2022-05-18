"""
Starts the game and displays the main menu (not yet)
"""

import pygame
from game import Game

class Tetris(object):
    def __init__(self):
        self.screen = pygame.display.set_mode([800, 480])

    def start_game(self):
        Game(self.screen)