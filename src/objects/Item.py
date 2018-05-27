#CK

import pygame
from resources import colours

class Item():
    def __init__(self, column, row):
        self.column = column
        self.row = row

        self.colour = colours.white

    def draw(self, surface, rect):
        pygame.draw.rect(surface, self.colour, rect)
