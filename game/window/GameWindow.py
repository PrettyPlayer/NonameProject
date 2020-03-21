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
				if event.key in (pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT):
					self.papich.changePos(event.key)
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
	
	def preInit(self):
		pygame.mixer.music.stop()
		self.backgroundMenuImage = Image()
		self.backgroundMenuImage.createStaticImage(960, 540, "center",
		                    "backgroundgameimage", "backgroundgame\\")
		self.papich = Papich()
		self.papich.createPapich(960, 380, 1/4, 1/4)
		
	def postInit(self):
		self.backgroundMenuImage.showStaticImage()
		self.papich.showPapich()
	
