# CK

import pygame
from pages.Page import Page
from resources import colours

class TransparentPage(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | Generate the semi transparent background to make a page of this nature
        self.backgroundSurface = self.createBackgroundSurface()

    def draw(self):
        self.surface.blit(self.backgroundSurface, (0, 0))
        self.drawObjects()

    def createBackgroundSurface(self):
        backgroundSurface = pygame.Surface((self.surface.get_width(), self.surface.get_height()))
        backgroundSurface.fill(colours.grey)
        backgroundSurface.set_alpha(7)

        return backgroundSurface
