import os
import pygame
from random import randint

class InitGame():
	def __init__(self):
		self.WIDTH = 1920
		self.HEIGHT = 1080
		self.fullscreen = 0
		self.visiblemouse = True
	def centeredwindow(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
	def preinitsound(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
	def initwindow(self):
		pygame.init()
		pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\2.png")))
		if self.fullscreen == 0:
			self.surf_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		elif self.fullscreen == 1:
			self.surf_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
		pygame.display.set_caption("Noname")
	def setvisisblemouse(self):
		pygame.mouse.set_visible(self.visiblemouse)
	def initstart(self):
		self.centeredwindow()
		self.preinitsound()
		self.initwindow()
		self.setvisisblemouse()
		self.menuwindow = Window(60)
		self.menuwindow.start()

class Window():
	def __init__(self, FPS):
		self.run = True
		self.FPS = FPS
	def start(self):
		self.clock = pygame.time.Clock()
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
			print('hello')
			pygame.display.update()
			self.clock.tick(self.FPS)

if __name__ == "__main__":
	theGame = InitGame()
	theGame.initstart()