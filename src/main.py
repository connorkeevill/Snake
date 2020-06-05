# CK

import os

import pygame

import Helpers
from Router import Router

os.environ['SDL_VIDEO_CENTERED'] = '1'  # | This centers the window
pygame.init()

screenWidth = 900
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake")

FPS = 60  # | The FPS to use
clock = pygame.time.Clock()

pages = ["MainMenu", "Play", "Pause", "GameOver"]

router = Router(screen)

page = router.route("MainMenu")
pageToResume = None

while True:
	page.update()
	page.draw()

	for event in pygame.event.get():
		action = page.handleEvent(event)

		if action in pages:
			if action == "Pause":
				page.pause()
				pageToResume = page

			page = router.route(action)

		elif action == "Resume":
			page = pageToResume
			page.unpause()

		Helpers.checkForQuit(event)

	pygame.display.update()
	clock.tick(FPS)
