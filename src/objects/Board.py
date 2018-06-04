#CK

from objects.Space import Space

class Board():
    def __init__(self, xPos, yPos, dimensions):
        self.xPos = xPos
        self.yPos = yPos
        self.width = dimensions['width']
        self.height = dimensions['height']

        # | Integer to count the number of collectible item that the board has
        self.collectibles = 0

        self.squareSideLength = 20
        self.squareBuffer = 3

        self.spaces = []
        self.createSpaces()

    # | draw()
    # |-------------------
    # | Draws the board.
    # |---------------
    def draw(self, surface):
        for row in self.spaces:
            for collumn in row:
                collumn.draw(surface)

    # | createSpaces()
    # |----------------------------------------------------
    # | Creates enough squares to populate the specified
    # | width and height of the board for the game.
    # |----------------------------------------
    def createSpaces(self):
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

        # | If the item is a collectible, then increase the count
        if item.type == 'collectible':
            self.collectibles += 1

    # | emptySquare()
    # |----------------------------------------------------------
    # | Takes an item and empties the space containing the item.
    # |------------------------------------------------------
    def emptySpaceWithItem(self, item):
        self.spaces[item.column][item.row].emptyContents()

        # | If the item is a collectible, then we need to decrease it's count
        if item.type == 'collectible':
            self.collectibles -= 1

    # | getSpace()
    # |------------------------------------------------
    # | Returns the space in the coordinates passed.
    # |------------------------------------------
    def getSpace(self, column, row):
        return self.spaces[column][row]

    # | getSnakeEnteredSpace()
    # |-----------------------------------------------------
    # | Returns the space that the snake has entered, and
    # | adjusts the collectible counter accordingly.
    # |-----------------------------------------
    def getSnakeEnteredSpace(self, column, row):
        space = self.getSpace(column, row)

        # | Try-catch to prevent error when the space is empty
        try:
            if space.item.type == 'collectible':
                self.collectibles -= 1
        except:
            pass

        return space



