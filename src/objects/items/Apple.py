#CK

from objects.items.Collectible import Collectible
from resources import colours

class Apple(Collectible):
    def __init__(self, column, row):
        Collectible.__init__(self, column, row)

        self.colour = colours.red
        self.eatenValue = 5
        self.scoreValue = 1