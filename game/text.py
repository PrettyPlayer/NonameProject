import os
import sys

import pygame

from game.image import Image

class Text(Image):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
	def loadtext(self, text, font, sizetext, color):
		self.text = pygame.font.Font("fonts\\" + font + ".ttf", sizetext)
		self.text = self.text.render(text, 1, color)
	
	def createrecttext(self, posx, posy):
		self.textrect = self.text.get_rect(center=(self.changex(posx), self.changey(posy)))
	
	
	def showtext(self, posx, posy):
		self.createrecttext(posx, posy)
		surf_main.blit(self.text, self.textrect)