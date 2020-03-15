import os

import pygame

from game.managegame import ManageGame
from game.registry import Registry, OPTIONS

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
		pygame.mouse.set_visible(OPTIONS.getReg("visiblemouse"))
	
	def initwindow(self):
		pygame.init()
		pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\papich\\2.png")))
		pygame.display.set_caption("Noname")
	
	
	def initstart(self):
		self.managegame = ManageGame()
		while True:
			self.managegame.update()