#CK

import pygame
import threading
import time
import random
from pages.Page import Page
from objects.Board import Board
from objects.snakeObjects.Snake import Snake
from objects.Apple import Apple

class Play(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | Flag to indicate if the snake has hit an item (and therefore another needs to be placed)
        self.itemHit = False
        # | Time that is between each movement of the snake (in seconds)
        self.movementInterval = 1 / 8

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
        snakeSquares = self.board
        self.snake = Snake(snakeColumn, snakeRow, snakeSquares)

        self.addToObjects(self.board)

        # | Place the first item
        self.placeNewItem()

        # | Start thread that moves the snake
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

        if self.itemHit:
            self.placeNewItem()

    # | placeNewItem()
    # |------------------------------------------------------
    # | Places a new item in a random location on the board.
    # |---------------------------------------------------
    def placeNewItem(self):
        column = random.randint(0, self.board.width - 1)
        row = random.randint(0, self.board.height - 1)

        item = Apple(column, row)
        self.board.giveItem(item)
        print("Apple Placed")

        self.itemHit = False

    # | moveSnake()
    # |-----------------------------------------------------
    # | Method to be called in a thread to move the snake.
    # |------------------------------------------------
    def moveSnake(self):
        self.itemHit = self.snake.move(self.board)
        time.sleep(self.movementInterval)
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
