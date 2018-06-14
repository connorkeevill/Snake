#CK

import pygame
import threading
import time
import random
from pages.Page import Page
from objects.Board import Board
from objects.snakeObjects.Snake import Snake
from objects.items.Apple import Apple

class Play(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | Flag to indicate if the snake has hit an item (and therefore another needs to be placed)
        self.itemHit = False
        # | Time that is between each movement of the snake (in seconds)
        self.movementInterval = 1 / 14

        # | board
        # |--------
        boardXpos = 20
        boardYpos = 20
        boardDimensions = {'width': 48, 'height': 28}
        boardSpaceSideLength = 17
        boardSpaceBuffer = 1
        self.board = Board(boardXpos, boardYpos, boardDimensions, boardSpaceSideLength, boardSpaceBuffer)

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

        # | Start the thread that places items in the board
        itemPlacer = threading.Thread(target=self.placeItems)
        itemPlacer.start()

    # | update()
    # |--------------------------------------------------
    # | Code to update the page. Essentially code that
    # | is neither drawing the page, or handling
    # | events, but code that still needs to
    # | be ran each loop of the game.
    # |-------------------------
    def update(self):
        self.changeSnakeDirection()

        # | If there is less than one collectible on the board, place another
        if self.board.collectibles < 1:
            self.placeNewItem()

    # | placeNewItem()
    # |------------------------------------------------------
    # | Places a new item in a random location on the board.
    # |---------------------------------------------------
    def placeNewItem(self):
        spaceOccupied = True

        # | Ensure that the new item is placed in an empty space
        while spaceOccupied:
            column = random.randint(0, self.board.width - 1)
            row = random.randint(0, self.board.height - 1)

            # | If the square is empty
            if self.board.getSpace(column, row).isEmpty():
                spaceOccupied = False

        item = Apple(column, row)
        self.board.giveItem(item)

        # | Reset the flag to place an item
        self.itemHit = False

    # | moveSnake()
    # |-----------------------------------------------------
    # | Method to be called in a thread to move the snake.
    # |------------------------------------------------
    def moveSnake(self):
        while self.snake.isAlive:
            self.snake.move(self.board)
            time.sleep(self.movementInterval)

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

    # | placeItem()
    # |----------------------------------------------------
    # | Makes a random decision to place an item on the
    # | board every random interval (between 1 and 5
    # | seconds, with a 1 in 5 chance each time).
    # |-------------------------------------
    def placeItems(self):
        while self.snake.isAlive:
            timeToWait = random.randint(1, 5)
            chance = random.randint(1, 5)
            if chance == 1:
                self.placeNewItem()
            time.sleep(timeToWait)
