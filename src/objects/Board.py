#CK

from objects.Space import Space

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

    # | draw()
    # |-------------------
    # | Draws the board.
    # |---------------
    def draw(self, surface):
        for row in self.squares:
            for collumn in row:
                collumn.draw(surface)

    # | populateSquares()
    # |----------------------------------------------------
    # | Creates enough squares to populate the specified
    # | width and height of the board for the game.
    # |----------------------------------------
    def populateSquares(self):
        for column in range(self.width):
            columnXpos = self.yPos + (column * (20 + self.squareBuffer))
            column = []
            for row in range(self.height):
                rowYpos = self.xPos + (row * (20 + self.squareBuffer))
                column.append(Space(columnXpos, rowYpos, self.squareSideLength))
            self.squares.append(column)


