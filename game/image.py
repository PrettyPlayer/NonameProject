import os
import sys

from random import randint
import pygame

class Image(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
	def loadimage(self, path, name):
		self.image = pygame.image.load(os.path.realpath(path + str(name) + ".png")).convert_alpha()
	
	def scale(self, sizex=1, sizey=1):
		self.image = pygame.transform.scale(self.image, (round(self.image.get_width()*self.changesizex(sizex)), round(self.image.get_height()*self.changesizey(sizey))))
	
	def createrectimage(self, posx, posy, pos="center"):
		if pos == "center":
			self.rect = self.image.get_rect(center=(self.changex(posx), self.changey(posy)))
		elif pos == "top":
			self.rect = self.image.get_rect(top=(self.changex(posx), self.changey(posy)))
		elif pos == "topleft":
			self.rect = self.image.get_rect(topleft=(self.changex(posx), self.changey(posy)))
		elif pos == "topright":
			self.rect = self.image.get_rect(topright=(self.changex(posx), self.changey(posy)))
		elif pos == "left":
			self.rect = self.image.get_rect(left=(self.changex(posx), self.changey(posy)))
		elif pos == "right":
			self.rect = self.image.get_rect(right=(self.changex(posx), self.changey(posy)))
		elif pos == "bottom":
			self.rect = self.image.get_rect(bottom=(self.changex(posx), self.changey(posy)))
		elif pos == "bottomleft":
			self.rect = self.image.get_rect(bottomleft=(self.changex(posx), self.changey(posy)))
		elif pos == "bottomright":
			self.rect = self.image.get_rect(bottomright=(self.changex(posx), self.changey(posy)))
	
	def changex(self, x):
		return(round(x/1920*width))
	
	def changey(self, y):
		return(round(y/1080*height))
	
	def changesizex(self, sizex):
		if width>1920:
			return(sizex*width/1920)
		else:
			return(sizex)
	
	def changesizey(self, sizey):
		if height>1080:
			return(sizey*height/1080)
		else:
			return(sizey)
	
	
	def createimage(self, path, name, sizex=1, sizey=1):
		self.loadimage(path, name)
		self.scale(sizex, sizey)
	
	def showimage(self, posx, posy, pos="center"):
		self.pos=pos
		self.createrectimage(posx, posy, self.pos)
		surf_main.blit(self.image, self.rect)