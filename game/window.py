import os
import pygame
from random import randint

class Window():
	def __init__(self):
		self.run = True
	def start(self, FPS):
		self.clock = pygame.time.Clock()
		self.preinit()
		while self.run:
			self.postinit()
			self.exit()
			pygame.display.update()
			self.clock.tick(FPS)
	def exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
				sys.exit()

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