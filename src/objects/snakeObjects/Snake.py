#CK

from objects.snakeObjects.Segment import Segment

class Snake():
    def __init__(self, column, row, board):
        self.column = column
        self.row = row
        self.direction = 'down'

        self.body = []
        self.placeHead(board)

        self.lengthToGrow = 0

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
    # | event that the item should cause, and returns a
    # | flag to indicate that something had been hit.
    # |------------------------------------------
    def checkNextSpaceForItem(self, board):
        item = board.spaces[self.column][self.row].getItem()

        try:
            self.lengthToGrow += item.getEatenValue()
            hit = True
        except:
            hit = False

        return hit

    # | move()
    # |--------------------------------------------------------
    # | Moves the snake in its current direction and returns
    # | a flag to indicate whether an item has been hit.
    # |--------------------------------------------
    def move(self, board):
        self.moveTail(board)
        self.moveHead()

        hit = self.checkNextSpaceForItem(board)

        self.placeHead(board)

        return hit

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
        directions = ['down', 'up', 'right', 'left']

        if newDirection in directions:
            self.direction = newDirection
