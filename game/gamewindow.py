import os
import sys

import pygame

from game.Window import Window
from game.Image import Image
from game.Text import Text
from game.Button import Button
from game.Animation import Animation
from game.Music import Music
from game.Sound import Sound
from game.Colors import Colors, COLOR
from game.Registry import Registry, OPTIONS

class GameWindow(Window):
	def __init__(self):
		self.scene = 1
		self.run = True
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()
	
	
	def preInit(self):
		pygame.mixer.music.stop()
	
	def postInit(self):
		pass
	
