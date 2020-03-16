import os
import sys

from random import randint
import pygame

from game.system.Registry import Registry, OPTIONS

class Image(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
	def loadImage(self, name, path=None):
		try:
			self.image = pygame.image.load(os.path.realpath("img\\" + path + str(name) + ".png")).convert_alpha()
		except:
			try:
				self.image = pygame.image.load(os.path.realpath("img\\" + str(name) + ".png")).convert_alpha()
			except:
				self.image = pygame.image.load(os.path.realpath("img\\" + path + str(name) + ".jpeg")).convert_alpha()
	def scaleImage(self, sizeX=1, sizeY=1):
		print(sizeX, sizeY)
		self.image = pygame.transform.scale(self.image, (round(self.image.get_width()*self.changeSizeX(sizeX)), round(self.image.get_height()*self.changeSizeY(sizeY))))
	
	def changeRectImage(self, posX, posY, pos="center"):
		if pos == "center":
			self.rect = self.image.get_rect(center=(self.changeX(posX), self.changeY(posY)))
		elif pos == "top":
			self.rect = self.image.get_rect(top=(self.changeX(posX), self.changeY(posY)))
		elif pos == "topleft":
			self.rect = self.image.get_rect(topleft=(self.changeX(posX), self.changeY(posY)))
		elif pos == "topright":
			self.rect = self.image.get_rect(topright=(self.changeX(posX), self.changeY(posY)))
		elif pos == "left":
			self.rect = self.image.get_rect(left=(self.changeX(posX), self.changeY(posY)))
		elif pos == "right":
			self.rect = self.image.get_rect(right=(self.changeX(posX), self.changeY(posY)))
		elif pos == "bottom":
			self.rect = self.image.get_rect(bottom=(self.changeX(posX), self.changeY(posY)))
		elif pos == "bottomleft":
			self.rect = self.image.get_rect(bottomleft=(self.changeX(posX), self.changeY(posY)))
		elif pos == "bottomright":
			self.rect = self.image.get_rect(bottomright=(self.changeX(posX), self.changeY(posY)))
	
	def changeX(self, x):
		return(round(x/1920*OPTIONS.getReg("width")))
	
	def changeY(self, y):
		return(round(y/1080*OPTIONS.getReg("height")))
	
	def changeSizeX(self, sizeX):
		if OPTIONS.getReg("width")>1920:
			return(sizeX*OPTIONS.getReg("width")/1920)
		else:
			return(sizeX)
	
	def changeSizeY(self, sizeY):
		if OPTIONS.getReg("height")>1080:
			return(sizeY*OPTIONS.getReg("height")/1080)
		else:
			return(sizeY)
	
	
	def createStaticImage(self, posX, posY, pos, name, path=None, sizeX=1, sizeY=1):
		self.path = path
		self.loadImage(name, self.path)
		self.scaleImage(sizeX, sizeY)
		self.changeRectImage(posX, posY, pos)
	
	def showStaticImage(self):
		OPTIONS.getReg("surf_main").blit(self.image, self.rect)
	
	def createImage(self, name, path=None, sizeX=1, sizeY=1):
		self.path = path
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.loadImage(name, self.path)
		self.scaleImage(sizeX, sizeY)
	
	def showImage(self, posX, posY, pos="center"):
		self.changeRectImage(posX, posY, pos)
		self.showStaticImage()