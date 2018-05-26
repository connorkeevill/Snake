#CK

import pygame
from resources import colours

class Square():
    def __init__(self, xPos, yPos, sideLength):
        self.rect = pygame.Rect(xPos, yPos, sideLength, sideLength)

        self.colour = colours.white
        self.hoverColour = colours.veryLightGrey
        self.drawColour = colours.white

        self.isHovering = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.drawColour, self.rect)

    def hover(self, xMouse, yMouse):
        self.isHovering = self.rect.collidepoint(xMouse, yMouse)

        if self.isHovering:
            self.drawColour = self.hoverColour
        else:
            self.drawColour = self.colour
