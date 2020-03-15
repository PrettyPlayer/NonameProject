import os
import sys

import pygame

class Sound():
	
	def __init__(self, path, name):
		self.sound = pygame.mixer.Sound(path + name + ".wav")
	
	def play(self, times):
		self.channel = self.sound.play()
	
	def stop(self):
		self.channel=self.stop()
	
	
	def start(self, time=300, times=-1):
		self.pauseupload(time)
		self.play(times)