#CK

from pages.MainMenu import MainMenu
from pages.Play import Play
from pages.GameOver import GameOver


class Router:
    def __init__(self, screen):
        self.screen = screen
        self.page = None

        self.routes = {"MainMenu":self.createMainMenu,
                       "Play":self.createPlay,
                       "GameOver":self.createGameOver}

    # | route()
    # |----------------------------------------------------
    # | Returns a new instance of the class relating to
    # | the route that was passed into the method
    # |-------------------------------------
    def route(self, route):
        self.page = route
        return self.routes[route]()

    def createMainMenu(self):
        return MainMenu(self.screen, self.page)

    def createPlay(self):
        return Play(self.screen, self.page)

    def createGameOver(self):
        return GameOver(self.screen, self.page)
