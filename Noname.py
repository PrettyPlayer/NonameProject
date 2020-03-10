import os
import pygame
from random import randint

class InitGame():
	def __init__(self):
		self.WIDTH = 1920
		self.HEIGHT = 1080
		self.fullscreen = 0
		self.visiblemouse = True
		self.rungame = True
		
		self.centeredwindow()
		self.preinitsound()
		self.initwindow()
		self.setvisisblemouse()
		self.managegame = ManageGame()
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
		while self.rungame:
			self.managegame.update()
		quit()
		sys.exit()

class Window():
	def __init__(self, FPS):
		self.run = True
		self.FPS = FPS
	def start(self):
		self.clock = pygame.time.Clock()
		self.preinit()
		while self.run:
			self.postinit()
			self.exit()
			pygame.display.update()
			self.clock.tick(self.FPS)
	def exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				thegame.managegame.scene = 0
				self.run = False

class MenuWindow(Window):
	def preinit(self):
		pass
	def postinit(self):
		pass

class GameWindow(Window):
	def preinit(self):
		pass
	def postinit(self):
		pass

class ManageGame():
	def __init__(self):
		self.scene = 1
		self.gamewindow = GameWindow(60)
		self.menuwindow = MenuWindow(60)
	def update(self):
		if self.scene == 0:
			thegame.rungame = False
		elif self.scene == 1:
			self.menuwindow.start()
		elif self.scene == 2:
			self.gamewindow.start()

if __name__ == "__main__":
	thegame = InitGame()
	thegame.initstart()