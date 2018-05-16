#CK

from pages.MainMenu import MainMenu


class Router:
    def __init__(self, screen):
        self.screen = screen
        self.page = None

        self.routes = {"MainMenu":self.createMainMenu}

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
