import os
import sys

import pygame

from game.window import Window
from game.image import Image
from game.text import Text
from game.button import Button
from game.animation import Animation
from game.music import Music
from game.sound import Sound
from game.COLORS import Colors, COLOR
from game.registry import Registry, OPTIONS

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
	
