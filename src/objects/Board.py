#CK

from objects.Square import Square

class Board():
    def __init__(self, xPos, yPos, dimensions):
        self.xPos = xPos
        self.yPos = yPos
        self.width = dimensions['width']
        self.height = dimensions['height']

        self.squareSideLength = 20
        self.squares = []
        self.squareBuffer = 3
        self.populateSquares()

    # | populateSquares()
    # |----------------------------------------------------
    # | Creates enough squares to populate the specified
    # | width and height of the board for the game.
    # |----------------------------------------
    def populateSquares(self):

        for row in range(self.height):
            rowYpos = self.yPos + (row * (20 + self.squareBuffer))
            row = []
            for collumn in range(self.width):
                collumnXpos = self.xPos + (collumn * (20 + self.squareBuffer))
                row.append(Square(collumnXpos, rowYpos, self.squareSideLength))
            self.squares.append(row)

    # | draw()
    # |-------------------
    # | Draws the board.
    # |---------------
    def draw(self, surface):
        for row in self.squares:
            for collumn in row:
                collumn.draw(surface)

    # | hover()
    # |----------------------------------------------------------
    # | Allows the squares to change colour with mouse movement.
    # |-------------------------------------------------------
    def hover(self, xMouse, yMouse):
        for row in self.squares:
            for collumn in row:
                collumn.hover(xMouse, yMouse)
