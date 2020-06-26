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
	
	def playSnd(self):
		self.channelPlay = OPTIONS.getReg("currentChannel")
		pygame.mixer.Channel(self.channelPlay).play(self.sound)
		if self.channelPlay < 19:
			OPTIONS.setReg("currentChannel", self.channelPlay + 1)
		elif self.channelPlay == 19:
			OPTIONS.setReg("currentChannel", 0)
	def stopSnd(self, strFade):
		pygame.mixer.Channel(self.channelPlay).fadeout(strFade)