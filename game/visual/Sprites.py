import os
import sys

import pygame

from game.visual.Image import Image
from game.system.Registry import Registry, OPTIONS

class Sprites(Image):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
	def genList(self):
		self.image={x: Image() for x in range(1, self.num+1)}
		
	def updateTime(self):
		self.currentTime += 1
	
	def createImages(self, path, posX, posY, sizeX=1, sizeY=1):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.posX = posX
		self.genList()
		for i in range(1, self.num+1):
			self.image[i].createImage(i, path, self.sizeX, self.sizeY)
			self.changeRect(i, posX, posY)