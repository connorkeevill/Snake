# CK

import pygame
import os
from src import Helpers
from src.Router import Router

os.environ['SDL_VIDEO_CENTERED'] = '1'  # | This centers the window
pygame.init()

screenWidth = 900
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("""The caption""")

FPS = 0  # | The FPS to use
clock = pygame.time.Clock()

pages = ["MainMenu", "Play"]

router = Router(screen)

page = router.route("MainMenu")
pageToResume = None

while True:
    page.update()
    page.draw()

    for event in pygame.event.get():
        action = page.handleEvent(event)

        if action in pages:
            page = router.route(action)

        Helpers.checkForQuit(event)

    pygame.display.update()
    clock.tick(FPS)

