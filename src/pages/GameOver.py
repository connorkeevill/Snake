# CK

from pages.TransparentPage import TransparentPage
from resources import colours
from objects.interfaceElements.Button import Button
from objects.interfaceElements.Title import Title

class GameOver(TransparentPage):
    def __init__(self, surface, pageName):
        TransparentPage.__init__(self, surface, pageName)

        # | btnPlayAgain
        # | --------------
        btnPlayAgainXpos = 450
        btnPlayAgainYpos = 250
        btnPlayAgainDmensions = {'width': 450, 'height': 100}
        btnPlayAgainColour = colours.buttonColour
        btnPlayAgainHoverColour = colours.buttonHoverColour
        btnPlayAgainAction = "Play"
        btnPlayAgainText = "Play again"
        btnPlayAgainTextSize = 28
        btnPlayAgainTextColour = colours.white
        btnPlayAgain = Button(btnPlayAgainXpos, btnPlayAgainYpos, btnPlayAgainDmensions, btnPlayAgainColour,
                              btnPlayAgainHoverColour, btnPlayAgainAction, btnPlayAgainText, btnPlayAgainTextSize,
                              btnPlayAgainTextColour)

        # | btnMainMenu
        # | --------------
        btnMainMenuXpos = 450
        btnMainMenuYpos = 400
        btnMainMenuDmensions = {'width': 450, 'height': 100}
        btnMainMenuColour = colours.buttonColour
        btnMainMenuHoverColour = colours.buttonHoverColour
        btnMainMenuAction = "MainMenu"
        btnMainMenuText = "Main Menu"
        btnMainMenuTextSize = 28
        btnMainMenuTextColour = colours.white
        btnMainMenu = Button(btnMainMenuXpos, btnMainMenuYpos, btnMainMenuDmensions, btnMainMenuColour,
                              btnMainMenuHoverColour, btnMainMenuAction, btnMainMenuText, btnMainMenuTextSize,
                              btnMainMenuTextColour)

        # | ttlGameOver
        # |--------------
        ttlGameOverXpos = 450
        ttlGameOverYpos = 125
        ttlGameOverText = "Game Over!"
        ttlGameOverTextSize = 70
        ttlGameOverTextColour = colours.red
        ttlGameOver = Title(ttlGameOverXpos, ttlGameOverYpos, ttlGameOverText, ttlGameOverTextSize, ttlGameOverTextColour)

        self.addToObjects([btnPlayAgain, btnMainMenu, ttlGameOver])
        self.addToButtons([btnPlayAgain, btnMainMenu])