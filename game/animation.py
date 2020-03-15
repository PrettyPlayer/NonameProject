import os
import sys

import pygame

from game.image import Image
from game.registry import Registry, OPTIONS

class Animation(Image):
	
	def __init__(self, path, num):
		self.currenttime=0
		self.currentnum=1
		self.maxnum=num
		self.image={}
		self.path=path
	
	def get(self, posx, posy, sizex=1, sizey=1):
		self.posx = posx
		self.posy = posy
		self.sizex = sizex
		self.sizey = sizey
	
	def genlist(self):
		self.image={x: Image() for x in range(1, self.maxnum+1)}
	
	def updatenum(self):
		if 0<self.currentnum<self.maxnum:
			self.currentnum+=1
		elif self.currentnum == self.maxnum:
			self.currentnum = 1
		else:
			print("Error updatenum()")
	
	def updatetime(self):
		self.currenttime+=1
	
	def changespeed(self, speed):
		return(round(speed*OPTIONS.getReg("fps")/60))
	
	def loadallimage(self, sizex=1, sizey=1):
		self.genlist()
		for i in range(1, self.maxnum+1):
			self.image[i].createimage(self.path, i, sizex, sizey)
	
	
	def showanimation(self, posx, posy, speed):
		if self.currenttime%self.changespeed(speed) == 0:
			self.image[self.currentnum].showimage(posx, posy)
			self.updatenum()
		self.updatetime()