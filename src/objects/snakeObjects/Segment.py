#CK

from resources import colours
from objects.Item import Item

# | Segment()
# |------------------------------------
# | The item that'll be used to make
# | up the body of of the snake.
# |-------------------------
class Segment(Item):
    def __init__(self, column, row):
        Item.__init__(self, column, row)

        self.colour = colours.green

    def hitSnake(self, snake):
        snake.die()
