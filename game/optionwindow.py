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

class OptionWindow(Window):
	def __init__(self):
		self.scene = 2
		self.run = True
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()
	
	
	def preInit(self):
		pass
	
	def postInit(self):
		pass
	
