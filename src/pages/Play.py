#CK

import pygame
import threading
import time
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

        snakeMover = threading.Thread(target=self.moveSnake)
        snakeMover.start()

    # | update()
    # |--------------------------------------------------
    # | Code to update the page. Essentially code that
    # | is neither drawing the page, or handling
    # | events, but code that still needs to
    # | be ran each loop of the game.
    # |-------------------------
    def update(self):
        self.changeSnakeDirection()

    # | moveSnake()
    # |-----------------------------------------------------
    # | Method to be called in a thread to move the snake.
    # |------------------------------------------------
    def moveSnake(self):
        self.snake.move(self.board.squares)
        time.sleep(0.25)
        self.moveSnake()

    # | changeSnakeDirection()
    # |----------------------------------------
    # | Changes the direction the snake moves
    # | based on the keys that are pressed.
    # |---------------------------------
    def changeSnakeDirection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.snake.changeDirection('down')
        elif keys[pygame.K_UP]:
            self.snake.changeDirection('up')
        elif keys[pygame.K_RIGHT]:
            self.snake.changeDirection('right')
        elif keys[pygame.K_LEFT]:
            self.snake.changeDirection('left')
