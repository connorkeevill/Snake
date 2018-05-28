#CK

import pygame
from resources import colours

# | Item()
# |--------------------------------------
# | The parent class for an item that
# | can fill a Space() object.
# |---------------------
class Item():
    def __init__(self, column, row):
        self.column = column
        self.row = row

        self.colour = colours.white

    # | draw()
    # |----------------------------------
    # | Draws the item to the screen.
    # |---------------------------
    def draw(self, surface, rect):
        pygame.draw.rect(surface, self.colour, rect)
