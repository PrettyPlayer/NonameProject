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
from game.system.Registry import Registry, OPTIONS

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
	
