#CK

import pygame
from pages.Page import Page
from objects.Board import Board
from objects.snakeObjects.Snake import Snake

class Play(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | board
        # |--------
        boardXpos = 20
        boardYpos = 20
        boardDimensions = {'width':37, 'height':23}
        self.board = Board(boardXpos, boardYpos, boardDimensions)

        # | snake
        # |--------
        snakeColumn = 10
        snakeRow = 10
        snakeSquares = self.board.squares
        self.snake = Snake(snakeColumn, snakeRow, snakeSquares)

        self.addToObjects(self.board)