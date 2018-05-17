#CK

from objects.Square import Square

class Board():
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.squares = []

        self.squareBuffer = 5
        self.populateSquares()

    def populateSquares(self):
        for row in range(20):
            rowYpos = self.yPos + (row * (20 + self.squareBuffer))
            row = []
            for collumn in range(20):
                collumnXpos = self.xPos + (collumn * (20 + self.squareBuffer))
                row.append(Square(collumnXpos, rowYpos))
            self.squares.append(row)

    def draw(self, surface):
        for row in self.squares:
            for collumn in row:
                collumn.draw(surface)

    def hover(self, xMouse, yMouse):
        for row in self.squares:
            for collumn in row:
                collumn.hover(xMouse, yMouse)
