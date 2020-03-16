import os
import sys

import pygame

from game.visual.Image import Image
from game.system.Registry import Registry, OPTIONS

class Animation(Image):
	
	def __init__(self, path, num):
		self.currentTime = 0
		self.currentNum = 1
		self.maxNum = num
		self.image = {}
		self.path = path
	
	def get(self, posX, posY, sizeX=1, sizeY=1):
		self.posX = posX
		self.posY = posY
		self.sizeX = sizeX
		self.sizeY = sizeY
	
	def genList(self):
		self.image={x: Image() for x in range(1, self.maxNum+1)}
	
	def updateNum(self):
		if 0<self.currentNum<self.maxNum:
			self.currentNum += 1
		elif self.currentNum == self.maxNum:
			self.currentNum = 1
		else:
			print("Error updateNum()")
	
	def updateTime(self):
		self.currentTime += 1
	
	def changeSpeed(self, speed):
		return(round(speed*OPTIONS.getReg("fps")/60))
	
	def createStaticAnimation(self, posX, posY, pos, sizeX=1, sizeY=1):
		self.genList()
		for i in range(1, self.maxNum+1):
			self.image[i].createStaticImage(posX, posY, pos, i, self.path, sizeX, sizeY)
	
	def showStaticAnimation(self, speed):
		if self.currentTime%self.changeSpeed(speed) == 0:
			self.updateNum()
		self.image[self.currentNum].showStaticImage()
		self.updateTime()
	
	def createAnimation(self, sizeX=1, sizeY=1):
		self.genList()
		for i in range(1, self.maxNum+1):
			self.image[i].createImage(i, self.path, sizeX, sizeY)
	
	def showAnimation(self, posX, posY, speed):
		if self.currentTime%self.changeSpeed(speed) == 0:
			self.updateNum()
		self.image[self.currentNum].showImage(posX, posY)
		self.updateTime()