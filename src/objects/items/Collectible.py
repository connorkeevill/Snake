# CK

from objects.items.Item import Item

class Collectible(Item):
    def __init__(self, column, row):
        Item.__init__(self, column, row)

        self.eatenValue = 0 # | The length that the snake should grow when eaten
        self.scoreValue = 0 # | The score that the snake will gain when eaten

        self.type = 'collectible'

    # | hitSnake()
    # |----------------------------------------------------
    # | Defines how the snake should act when it enters
    # | a space containing a Collectible type item.
    # |--------------------------------------
    def hitSnake(self, snake):
        snake.grow(self.eatenValue)
        snake.giveScore(self.scoreValue)
