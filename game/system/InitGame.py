import os

import pygame

from game.system.ManageGame import ManageGame
from game.system.Registry import Registry, OPTIONS

class InitGame(object):
	
	def __init__(self):
		self.centeredWindow()
		self.preInitSound()
		self.initWindow()
		self.setVisisbleMouse()
	
	def centeredWindow(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
	
	def preInitSound(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
	
	def setVisisbleMouse(self):
		pygame.mouse.set_visible(OPTIONS.getReg("visibleMouse"))
	
	def initWindow(self):
		pygame.init()
		pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\papich\\2.png")))
		pygame.display.set_caption("Noname")
	
	
	def initStart(self):
		self.manageGame = ManageGame()
		while True:
			self.manageGame.update()