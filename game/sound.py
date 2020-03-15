import os
import sys

import pygame

class Sound():
	
	def __init__(self, name, path=None):
		try:
			self.sound = pygame.mixer.Sound("sfx\\" + path + name + ".wav")
		except:
			self.sound = pygame.mixer.Sound("sfx\\" + name + ".wav")
	
	def play(self):
		self.channel = self.sound.play()
	
	def stop(self):
		self.channel=self.stop()