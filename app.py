import os, pygame, math, random
from pygame.locals import *
from settings import Settings
from game import Game

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():

	pygame.init()
	screen = pygame.display.set_mode((Settings.width, Settings.height))
	pygame.display.set_caption(Settings.title)

	game = Game()
	game.loop(screen)
	game.quit()

	pygame.quit()

if __name__ == '__main__':
	main()