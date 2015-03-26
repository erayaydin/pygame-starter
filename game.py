import os, pygame

from settings import Settings

class Game():
	def __init__(self):
		pass

	def loop(self, screen):
		clock = pygame.time.Clock()

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))

			pygame.display.update()

	def quit(self):
		pass