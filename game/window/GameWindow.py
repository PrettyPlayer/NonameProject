import os
import sys

import pygame

from game.window.Window import Window
from game.visual.Image import Image
from game.visual.Text import Text
from game.visual.Button import Button
from game.visual.Animation import Animation
from game.visual.Music import Music
from game.visual.Sound import Sound
from game.visual.Colors import Colors, COLOR
from game.object.Papich import Papich
from game.system.Registry import Registry, OPTIONS

class GameWindow(Window):
	def __init__(self):
		self.scene = 1
		self.run = True
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == (pygame.K_LEFT or pygame.K_DOWN or pygame.K_RIGHT):
					papich.changePos(event.key)
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
	
	def preInit(self):
		pygame.mixer.music.stop()
		papich = Papich("papich\\", 3)
		papich.createPapich(960, 800)
	def postInit(self):
		papich.showPapich()
	
