import os

import pygame

from game.managegame import ManageGame
from game.registry import Reg

class InitGame(object):
	
	def __init__(self):
		self.centeredwindow()
		self.preinitsound()
		self.initwindow()
		self.setvisisblemouse()
	
	def centeredwindow(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
	
	def preinitsound(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
	
	def setvisisblemouse(self):
		pygame.mouse.set_visible(self.visiblemouse)
	
	def fullscreenchange(self):
		if Reg.getreg("fullscreen") == 0:
			self.surf_main = pygame.display.set_mode((width, height))
		elif self.fullscreen == 1:
			self.surf_main = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
	
	def initwindow(self):
		pygame.init()
		pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\papich\\2.png")))
		self.fullscreenchange()
		pygame.display.set_caption("Noname")
	
	
	def initstart(self, copy):
		self.managegame = ManageGame(copy)
		while self.rungame:
			self.managegame.update()