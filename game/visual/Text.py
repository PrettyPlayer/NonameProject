import os
import sys

import pygame

from game.visual.Image import Image
from game.system.Registry import Registry, OPTIONS

class Text(Image):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
	def changeRectText(self, posX, posY):
		self.textRect = self.text.get_rect(center=(self.changeX(posX), self.changeY(posY)))
	
	
	def createStaticText(self, text, font, sizeText, color, posX, posY):
		self.createText(text, font, sizeText, color)
		self.changeRectText(posX, posY)
	
	def showStaticText(self):
		OPTIONS.getReg("surf_main").blit(self.text, self.textRect)
	
	def createText(self, text, font, sizeText, color):
		self.text = pygame.font.Font("fonts\\" + font + ".ttf", sizeText)
		self.text = self.text.render(text, 1, color)
	
	def showText(self, posX, posY):
		self.createRectText(posX, posY)
		OPTIONS.getReg("surf_main").blit(self.text, self.textRect)