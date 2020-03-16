import os
import sys

import pygame

from game.visual.Text import Text
from game.system.Registry import Registry, OPTIONS

class Button(Text):
	
	def __init__(self, name):
		self.name = name
		pygame.sprite.Sprite.__init__(self)
	
	def createButton(self, name, text, font, sizeText, color, sizeX=1, sizeY=1):
		self.sizeX=sizeX
		self.sizeY=sizeY
		self.createImage(name, "button\\", self.sizeX, self.sizeY)
		self.createText(text, font, sizeText, color)
	
	def showButton(self, posX, posY, pos="center"):
		self.showImage(posX, posY, pos)
		self.showText(posX, posY)
	
	def createStaticButton(self, name, posX, posY, pos, text, font, sizeText, color, sizeX=1, sizeY=1):
		self.sizeX=sizeX
		self.sizeY=sizeY
		self.createStaticImage(posX, posY, pos, name, "button\\", self.sizeX, self.sizeY)
		self.createStaticText(text, font, sizeText, color, posX, posY)
	
	def showStaticButton(self):
		self.showStaticImage()
		self.showStaticText()
	
	def click(self, mousePos):
		if self.rect[0] <= mousePos[0] <= self.rect[0]+self.rect[2] and self.rect[1] <= mousePos[1] <= self.rect[1]+self.rect[3]:
			if self.name == "start":
				OPTIONS.setReg("scene", 1)
			elif self.name == "settings":
				OPTIONS.setReg("scene", 2)
			elif self.name == "exit":
				quit()
				sys.exit()