import os
import sys

import pygame

from game.registry import Registry, OPTIONS

class Window(object):
	
	def exit(self):
		quit()
		sys.exit()
	
	def preInitFullscreen(self):
		if OPTIONS.getReg("fullscreen") == 1:
			self.surf_main = pygame.display.set_mode((OPTIONS.getReg("width"), OPTIONS.getReg("height")), pygame.FULLSCREEN)
			OPTIONS.setReg("surf_main", self.surf_main)
		elif OPTIONS.getReg("fullscreen") == 0:
			self.surf_main = pygame.display.set_mode((OPTIONS.getReg("width"), OPTIONS.getReg("height")))
			OPTIONS.setReg("surf_main", self.surf_main)
	
	def changeFullscreen(self):
		if OPTIONS.getReg("fullscreen") == 1:
			self.surf_main = pygame.display.set_mode((OPTIONS.getReg("width"), OPTIONS.getReg("height")))
			OPTIONS.setReg("surf_main", self.surf_main)
			OPTIONS.setReg("fullscreen", 0)
		elif OPTIONS.getReg("fullscreen") == 0:
			self.surf_main = pygame.display.set_mode((OPTIONS.getReg("width"), OPTIONS.getReg("height")), pygame.FULLSCREEN)
			OPTIONS.setReg("surf_main", self.surf_main)
			OPTIONS.setReg("fullscreen", 1)
	
	def changeScene(self):
		if not(OPTIONS.getReg("scene") == self.scene):
			self.run = False
	
	def start(self, fps):
		self.fps = fps
		OPTIONS.setReg("fps", self.fps)
		self.clock = pygame.time.Clock()
		self.preInitFullscreen()
		self.preInit()
		while self.run:
			self.events()
			self.postInit()
			pygame.display.update()
			self.clock.tick(OPTIONS.getReg("fps"))
			self.changeScene()