#CK

from pages.TransparentPage import TransparentPage
from resources import colours
from objects.interfaceElements.Button import Button

class Pause(TransparentPage):
    def __init__(self, page, pageName):
        TransparentPage.__init__(self, page, pageName)

        # | btnResume
        # |------------
        btnResumeXpos = self.surface.get_width() // 2
        btnResumeYpos = 200
        btnResumeDimensions = {'width': 450, 'height': 100}
        btnResumeColour = colours.buttonColour
        btnResumeHoverColour = colours.buttonHoverColour
        btnResumeAction = "Resume"
        btnResumeText = "Resume"
        btnResumeTextSize = 28
        btnResumeTextColour = colours.white
        btnResume = Button(btnResumeXpos, btnResumeYpos, btnResumeDimensions, btnResumeColour, btnResumeHoverColour,
                              btnResumeAction, btnResumeText, btnResumeTextSize, btnResumeTextColour)

        # | btnResume
        # |------------
        btnMainMenuXpos = self.surface.get_width() // 2
        btnMainMenuYpos = 400
        btnMainMenuDimensions = {'width': 450, 'height': 100}
        btnMainMenuColour = colours.buttonColour
        btnMainMenuHoverColour = colours.buttonHoverColour
        btnMainMenuAction = "MainMenu"
        btnMainMenuText = "Main Menu"
        btnMainMenuTextSize = 28
        btnMainMenuTextColour = colours.white
        btnMainMenu = Button(btnMainMenuXpos, btnMainMenuYpos, btnMainMenuDimensions, btnMainMenuColour, btnMainMenuHoverColour,
                              btnMainMenuAction, btnMainMenuText, btnMainMenuTextSize, btnMainMenuTextColour)

        self.addToObjects([btnResume, btnMainMenu])
        self.addToButtons([btnResume, btnMainMenu])