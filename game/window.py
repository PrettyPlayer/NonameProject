import os
import sys

import pygame

from game.registry import Reg

CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

class Window(object):
	
	def __init__(self):
		self.run = True
	
	def exit(self):
		quit()
		sys.exit()
	
	
	def start(self, Frames):
		global FPS
		FPS = Frames
		self.clock = pygame.time.Clock()
		self.preinit()
		while self.run:
			self.postinit()
			pygame.display.update()
			self.clock.tick(FPS)