import os
import sys

import pygame

from game.visual.Sprites import Sprites
from game.visual.Image import Image
from game.system.Registry import Registry, OPTIONS

class Papich(Image):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.currentTime = 0
		self.nameimg = ("[1]", "[2]", "1", "2", "3")
		self.papichsurf = []
		for i in range(len(self.nameimg)):
			self.papichsurf.append(pygame.image.load(os.path.realpath("img\\" + "papich\\" + self.nameimg[i] + ".png")).convert_alpha())
		
	def createPapich(self, posX, posY, sizeX=1, sizeY=1):
		self.posX = posX
		self.posY = posY
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.image = self.papichsurf[1]
		self.scaleImage(self.sizeX, self.sizeY)
		self.changeRectImage(self.posX, self.posY)
		
	def shoot(self):
		pass
	def changePos(self, event):
		if event == pygame.K_LEFT:
			self.currentNum = 1
			self.image = self.papichsurf[4]
			self.scaleImage(self.sizeX, self.sizeY)
			self.changeRectImage(self.posX-50, self.posY)
			print("left")
		elif event == pygame.K_DOWN:
			self.currentNum = 2
			self.image = self.papichsurf[3]
			self.scaleImage(self.sizeX, self.sizeY)
			self.changeRectImage(self.posX, self.posY)
			print("center")
		elif event == pygame.K_RIGHT:
			self.currentNum = 3
			self.image = self.papichsurf[2]
			self.scaleImage(self.sizeX, self.sizeY)
			self.changeRectImage(self.posX+50, self.posY)
			print("right")
	def showPapich(self):
		self.showStaticImage()