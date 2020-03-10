import os, sys
import pygame
from random import randint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Noname import *

def x(x):
	return(round(x/1920*width))
def y(y):
	return(round(y/1080*height))
def sizex(sizex):
	return(round(width/1920))
def sizey(sizey):
	return(round(height/1080))

class Window():
	def __init__(self):
		self.run = True
	def start(self, FPS):
		self.clock = pygame.time.Clock()
		self.preinit()
		while self.run:
			self.postinit()
			self.exit()
			pygame.display.update()
			self.clock.tick(FPS)
	def exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
				sys.exit()

class MenuWindow(Window):
	def preinit(self):
		pass
	def postinit(self):
		pass

class GameWindow(Window):
	def preinit(self):
		pass
	def postinit(self):
		pass

class image():
	def __init__(self, path, posx, posy, sizex=1, sizey=1):
		self.image = pygame.image.load(os.path.realpath(path))
		self.image = pygame.transform.scale(self.image, (sizex, sizey))
		self.rect = self.image.get_rect(center=(posx, posy))
	def update(self):
		thegame.surf_main.blit(self.image, self.rect.rect)