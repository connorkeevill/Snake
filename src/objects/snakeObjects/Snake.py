#CK

from objects.snakeObjects.Segment import Segment

class Snake():
    def __init__(self, column, row, board):
        self.column = column
        self.row = row
        self.direction = 'down'

        self.body = []
        self.placeHead(board)

    # | placeHead()
    # |----------------------------------------
    # | Creates the snake's "head" and places
    # | it into the board to move the snake.
    # |----------------------------------
    def placeHead(self, board):
        head = Segment(self.column, self.row)

        self.body.append(head)
        board[self.column][self.row].giveItem(head)

    # | move()
    # |-------------------------------------------
    # | Moves the snake in its current direction.
    # |----------------------------------------
    def move(self, board):
        self.moveTail(board)
        self.moveHead()
        self.placeHead(board)

    # | moveTail()
    # |--------------------------------------------------------
    # | Removes the last segment of the snake to prepare for
    # | the head to move to its next space of the board.
    # |--------------------------------------------
    def moveTail(self, board):
        tailEnd = self.body[-1]
        board[tailEnd.column][tailEnd.row].emptyContents()
        self.body.pop(-1)

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
