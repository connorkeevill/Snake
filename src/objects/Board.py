# CK

from objects.Space import Space
from objects.items.Wall import Wall


class Board():
	def __init__(self, xPos, yPos, dimensions, spaceSideLength, spaceBuffer):
		self.xPos = xPos
		self.yPos = yPos
		self.width = dimensions['width']
		self.height = dimensions['height']
		self.spaceSideLength = spaceSideLength
		self.spaceBuffer = spaceBuffer

		# | Integer to count the number of collectible item that the board has
		self.collectibles = 0

		self.spaces = []
		self.createSpaces()
		self.createWalls()

	# | createWalls()
	# |-----------------------------------------------------
	# | Iterates through the spaces and fills all the edge
	# | spaces with a wall item to create a border.
	# |---------------------------------------
	def createWalls(self):
		for column in range(self.width):
			for row in range(self.height):
				if (column == 0) or (column == self.width - 1) or (row == 0) or (row == self.height - 1):
					wall = Wall(column, row)
					self.giveItem(wall)

	# | draw()
	# |-------------------
	# | Draws the board.
	# |---------------
	def draw(self, surface):
		for column in self.spaces:
			for space in column:
				space.draw(surface)

	# | createSpaces()
	# |----------------------------------------------------
	# | Creates enough squares to populate the specified
	# | width and height of the board for the game.
	# |----------------------------------------
	def createSpaces(self):
		for column in range(self.width):
			columnXpos = self.yPos + (column * (self.spaceSideLength + self.spaceBuffer))
			column = []
			for row in range(self.height):
				rowYpos = self.xPos + (row * (self.spaceSideLength + self.spaceBuffer))
				column.append(Space(columnXpos, rowYpos, self.spaceSideLength))
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
