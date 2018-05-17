#CK

import pygame
from pages.Page import Page
from objects.Board import Board

class Play(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | board
        # |--------
        boardXpos = 20
        boardYpos = 20
        self.board = Board(boardXpos, boardYpos)

        self.addToObjects(self.board)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            xMouse, yMouse = pygame.mouse.get_pos()
            self.board.hover(xMouse, yMouse)
