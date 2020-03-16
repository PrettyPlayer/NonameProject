import os
import sys

import pygame

from game.visual.Sprites import Sprites
from game.system.Registry import Registry, OPTIONS

class Papich(Sprites):
	def __init__(self, path, num):
		pygame.sprite.Sprite.__init__(self)
		self.currentTime = 0
		self.num = num
		self.image = {}
		self.path = path
	
	def createPapich(self, posX, posY, sizeX=1, sizeY=1):
		self.posX = posX
		self.posY = posY
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.createImages(self.path, posX, posY, self.sizeX, self.sizeY)
	def shoot(self):
		pass
	def changePos(self, event):
		if event == pygame.K_LEFT:
			self.currentNum = 1
		elif event == pygame.K_DOWN:
			self.currentNum = 2
		elif event == pygame.K_RIGHT:
			self.currentNum = 3
	def showPapich(self):
		self.image[self.currentNum].showImage(self.posX, self.posY)