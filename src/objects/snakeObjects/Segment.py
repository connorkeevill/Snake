#CK

from resources import colours
from objects.Item import Item

class Segment(Item):
    def __init__(self, column, row):
        Item.__init__(self, column, row)

        self.colour = colours.green