import os
import sys

import pygame

class Music():
	
	def __init__(self, name, path=None):
		try:
			self.music = pygame.mixer.music.load("music\\" + path + name + ".wav")
		except:
			self.music = pygame.mixer.music.load("music\\" + name + ".wav")
	
	def pauseUpload(self, time):
		self.music = pygame.time.wait(time)
	
	def play(self, times):
		self.music = pygame.mixer.music.play(times)
	
	def stop(self):
		self.music = pygame.mixer.music.stop()
	
	
	def start(self, time=300, times=-1):
		self.pauseUpload(time)
		self.play(times)