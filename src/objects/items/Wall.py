# CK

from objects.items.Item import Item
from resources import  colours

class Wall(Item):
    def __init__(self, column, row):
        Item.__init__(self, column, row)

        self.colour = colours.grey

    def hitSnake(self, snake):
        snake.die()