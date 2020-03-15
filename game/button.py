import os
import sys

import pygame

from game.text import Text
from game.registry import Registry, OPTIONS

class Button(Text):
	
	def __init__(self, name):
		self.name = name
		pygame.sprite.Sprite.__init__(self)
	
	def loadbutton(self, name, text, font, sizetext, color, sizex=1, sizey=1):
		self.sizex = sizex
		self.sizey = sizey
		self.createimage("img\\button\\", name, self.sizex, self.sizey)
		self.loadtext(text, font, sizetext, color)
	
	def showbutton(self, posx, posy, pos="center"):
		self.posx = posx
		self.posy = posy
		self.pos = pos
		self.showimage(posx, posy, self.pos)
		self.showtext(posx, posy)
	
	# Добавить gameevents!!
	def click(self, mousepos):
		if self.rect[0] <= mousepos[0] <= self.rect[0]+self.rect[2] and self.rect[1] <= mousepos[1] <= self.rect[1]+self.rect[3]:
			if self.name == "start":
				OPTIONS.setReg("scene", 1)
			elif self.name == "settings":
				OPTIONS.setReg("scene", 2)
			elif self.name == "exit":
				quit()
				sys.exit()