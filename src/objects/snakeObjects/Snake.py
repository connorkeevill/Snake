#CK

import pygame
from objects.snakeObjects.Segment import Segment
import random
from resources import Globals

class Snake():
    def __init__(self, column, row, board):
        self.column = column
        self.row = row
        self.direction = ''

        self.isAlive = True
        self.directions = ['down', 'up', 'right', 'left']

        self.body = []
        self.placeHead(board)

        self.score = 0
        self.lengthToGrow = 0

        self.chooseDirection()

    # | placeHead()
    # |----------------------------------------
    # | Creates the snake's "head" and places
    # | it into the board to move the snake.
    # |----------------------------------
    def placeHead(self, board):
        head = Segment(self.column, self.row)

        self.body.append(head)
        board.giveItem(head)

    # | checkNextSpaceForItem()
    # |-------------------------------------------------------
    # | Checks for any items in the next space, handles the
    # | effect that the item might have on the snake.
    # |------------------------------------------
    def checkNextSpaceForItem(self, board):
        space = board.getSnakeEnteredSpace(self.column, self.row)

        space.enterSnake(self)

    # | move()
    # |--------------------------------------------
    # | Moves the snake in its current direction.
    # |----------------------------------------
    def move(self, board):
        self.moveTail(board)
        self.moveHead()

        self.checkNextSpaceForItem(board)

        self.placeHead(board)

    # | moveTail()
    # |--------------------------------------------------------
    # | Removes the last segment of the snake to prepare for
    # | the head to move to its next space of the board.
    # |--------------------------------------------
    def moveTail(self, board):
        if self.lengthToGrow > 0:
            self.lengthToGrow -= 1
        else:
            tailEnd = self.body[0]
            board.emptySpaceWithItem(tailEnd)
            del self.body[0]

    # | moveHead()
    # |-------------------------------------------------------
    # | Alters the pointer of the snake's position preparing
    # | to place the head into its new space in the board.
    # |------------------------------------------------
    def moveHead(self):
        if self.direction == 'down':
            self.row += 1
        elif self.direction == 'up':
            self.row -= 1
        elif self.direction == 'right':
            self.column += 1
        elif self.direction == 'left':
            self.column -= 1

    # | changeDirection()
    # |------------------------------------------------
    # | Changes the direction of the snake's movement.
    # |---------------------------------------------
    def changeDirection(self, newDirection):
        if self.notHittingBody(newDirection):
            self.direction = newDirection

    # | notHittingBody()
    # |----------------------------------------------------------------------------------
    # | Returns a boolean indicating whether or not the proposed direction will place
    # | the snake's head into it's neck (the segment behind the head), to determine
    # | whether or not the proposed direction is safe for the snake to go in.
    # |------------------------------------------------------------------
    def notHittingBody(self, direction):
        if len(self.body) == 1:
            return True

        head = self.body[-1]
        headColumn = head.column
        headRow = head.row

        neck = self.body[-2]
        neckColumn = neck.column
        neckRow = neck.row

        # | This is a bit *ugly* but it works for now
        if direction == 'right':
            headColumn += 1
        elif direction == 'left':
            headColumn -= 1
        elif direction == 'down':
            headRow += 1
        elif direction == 'up':
            headRow -= 1

        return not (headColumn == neckColumn and headRow == neckRow)

    # | die()
    # |--------------------------------------------------------------
    # | Kills the snake. Used when the snake hits itself or a wall.
    # |---------------------------------------------------------
    def die(self):
        deathEvent = pygame.event.Event(Globals.DEADSNAKE)
        pygame.event.post(deathEvent)

        self.isAlive = False

    # | grow()
    # |------------------------------------------------
    # | Grows the snake by the amount that is passed.
    # |--------------------------------------------
    def grow(self, amount):
        self.lengthToGrow += amount

    # | giveScore()
    # |-------------------------------------------------------
    # | Takes a value and increases the snake's score by it.
    # |--------------------------------------------------
    def giveScore(self, amount):
        self.score += amount

    # | getScore()
    # |-----------------------------
    # | Returns the snake's score.
    # |------------------------
    def getScore(self):
        return self.score

    # | chooseDirection()
    # |------------------------------------------------------
    # | Selects a random direction of travel for the snake.
    # |-------------------------------------------------
    def chooseDirection(self):
        self.direction = random.choice(self.directions)
