#CK

from objects.Space import Space

class Board():
    def __init__(self, xPos, yPos, dimensions):
        self.xPos = xPos
        self.yPos = yPos
        self.width = dimensions['width']
        self.height = dimensions['height']

        self.squareSideLength = 20
        self.spaces = []
        self.squareBuffer = 3
        self.populateSpaces()

    # | draw()
    # |-------------------
    # | Draws the board.
    # |---------------
    def draw(self, surface):
        for row in self.spaces:
            for collumn in row:
                collumn.draw(surface)

    # | populateSpaces()
    # |----------------------------------------------------
    # | Creates enough squares to populate the specified
    # | width and height of the board for the game.
    # |----------------------------------------
    def populateSpaces(self):
        for column in range(self.width):
            columnXpos = self.yPos + (column * (20 + self.squareBuffer))
            column = []
            for row in range(self.height):
                rowYpos = self.xPos + (row * (20 + self.squareBuffer))
                column.append(Space(columnXpos, rowYpos, self.squareSideLength))
            self.spaces.append(column)

    # | giveItem()
    # |--------------------------------------------------
    # | Takes an item and puts it in the relevant space.
    # |-----------------------------------------------
    def giveItem(self, item):
        self.spaces[item.column][item.row].giveItem(item)

    # | emptySquare()
    # |----------------------------------------------------------
    # | Takes an item and empties the space containing the item.
    # |------------------------------------------------------
    def emptySpaceWithItem(self, item):
        self.spaces[item.column][item.row].emptyContents()


