#CK

from objects.Item import Item
from resources import colours

class Apple(Item):
    def __init__(self, column, row):
        Item.__init__(self, column, row)

        self.colour = colours.red
        self.eatenValue = 5

    # | hitSnake()
    # |----------------------------------------------------
    # | Defines how the snake should act when it enters
    # | a space containing and Apple() type item.
    # |--------------------------------------
    def hitSnake(self, snake):
        snake.grow(self.eatenValue)
