#CK

import pygame
from resources import colours

class Space():
    def __init__(self, xPos, yPos, sideLength):
        self.rect = pygame.Rect(xPos, yPos, sideLength, sideLength)

        self.colour = colours.white
        self.item = None

    # | draw()
    # |-------------------------------------
    # | Draws the space to the screen or
    # | the item the space may have.
    # |-------------------------
    def draw(self, surface):
        if self.item == None:
            pygame.draw.rect(surface, self.colour, self.rect)
        else:
            self.item.draw(surface, self.rect)

    # | giveItem()
    # |-------------------------------------
    # | Gives the space a new item object.
    # |-------------------------------
    def giveItem(self, item):
        self.item = item

    # | emptyContents()
    # |-------------------------------------
    # | Empties the contents of the space.
    # |--------------------------------
    def emptyContents(self):
        self.item = None

    # | getItem()
    # |-------------------------------------------
    # | Returns the item that the space may have.
    # |---------------------------------------
    def getItem(self):
        return self.item
