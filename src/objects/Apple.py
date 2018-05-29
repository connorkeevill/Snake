#CK

from objects.Item import Item
from resources import colours

class Apple(Item):
    def __init__(self, column, row):
        Item.__init__(self, column, row)

        self.colour = colours.red
        self.eatenValue = 5

    def getEatenValue(self):
        return self.eatenValue
