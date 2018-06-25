#CK

from resources import colours
from pages.Page import Page
from objects.interfaceElements.Button import Button
from objects.interfaceElements.Title import Title

class MainMenu(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | btnPlay
        # |---------------
        btnPlayXpos = 450
        btnPlayYpos = 350
        btnPlayDimensions = {"width": 250, "height": 100}
        btnPlayColour = colours.buttonColour
        btnPlayHoverColour = colours.buttonHoverColour
        btnPlayAction = "Play"
        btnPlayText = "Play"
        btnPlayTextSize = 28
        btnPlayTextColour = colours.white
        self.btnPlay = Button(btnPlayXpos, btnPlayYpos, btnPlayDimensions, btnPlayColour,
                              btnPlayHoverColour, btnPlayAction, btnPlayText, btnPlayTextSize, btnPlayTextColour)

        # | ttlSnake
        # |-----------
        ttlSnakeXpos = 450
        ttlSnakeYpos = 200
        ttlSnakeText = "Snake"
        ttlSnakeTextSize = 121
        self.ttlSnake = Title(ttlSnakeXpos, ttlSnakeYpos, ttlSnakeText, ttlSnakeTextSize)

        self.addToObjects([self.btnPlay, self.ttlSnake])
        self.addToButtons(self.btnPlay)
