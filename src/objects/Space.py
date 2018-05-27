#CK

import pygame
from resources import colours

class Space():
    def __init__(self, xPos, yPos, sideLength):
        self.rect = pygame.Rect(xPos, yPos, sideLength, sideLength)

        self.colour = colours.white
        self.item = None

    def draw(self, surface):
        if self.item == None:
            pygame.draw.rect(surface, self.colour, self.rect)
        else:
            self.item.draw(surface, self.rect)

    def giveItem(self, item):
        self.item = item

    def emptyContents(self):
        self.item = None

    def getItem(self):
        return self.item
