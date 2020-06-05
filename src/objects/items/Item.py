# CK

import pygame

from resources import colours


# | Item()
# |--------------------------------------
# | The parent class for an item that
# | can fill a Space() object.
# |---------------------
class Item():
	def __init__(self, column, row):
		self.column = column
		self.row = row

		self.colour = colours.white

		self.type = None

	# | draw()
	# |----------------------------------
	# | Draws the item to the screen.
	# |---------------------------
	def draw(self, surface, rect):
		pygame.draw.rect(surface, self.colour, rect)

	# | hitSnake()
	# |------------------------------------------------
	# | Place holder for the method that will handle
	# | the event of the snake hitting the item.
	# |--------------------------------------
	def hitSnake(self, snake):
		pass
