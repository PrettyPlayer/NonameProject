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

class GameWindow(Window):
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()
	
	
	def preinit(self):
		pass
	
	def postinit(self):
		pass
	
