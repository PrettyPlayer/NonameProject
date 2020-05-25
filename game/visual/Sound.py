import os
import sys

import pygame

from game.system.Registry import Registry, OPTIONS

class Sound():
	
	def __init__(self, name, path=None):
		self.name = name
		self.channelPlay = 0
		try:
			self.sound = pygame.mixer.Sound("sfx\\" + path + "\\" + name + ".wav")
		except:
			self.sound = pygame.mixer.Sound("sfx\\" + name + ".wav")
	
	def setVolume(self, vol):
		self.sound.set_volume(vol/100)
	
	def play(self):
		pygame.mixer.Channel(OPTIONS.getReg("currentChannel")).play(self.sound)
		self.channelPlay = OPTIONS.getReg("currentChannel")
		if self.channelPlay < 7:
			OPTIONS.setReg("currentChannel", self.channelPlay + 1)
		elif self.channelPlay == 7:
			OPTIONS.setReg("currentChannel", 0)
		
	def stop(self):
		pygame.mixer.Channel(self.channelPlay).fadeout(200)