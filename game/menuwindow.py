import os
import sys

import pygame

from game.window import Window
from game.image import Image
from game.text import Text
from game.button import Button
from game.animation import Animation
from game.music import Music
from game.sound import Sound
from game.COLORS import Colors, COLOR
from game.registry import Registry, OPTIONS

class MenuWindow(Window):
	def __init__(self):
		self.scene = 0
		self.run = True
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.startbutton.click(event.pos)
					self.settingsbutton.click(event.pos)
					self.exitbutton.click(event.pos)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pass
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
	
	def preInit(self):
		
		pygame.mixer.music.stop()
		self.time=0
		self.backgroundmusic = Music("sfx\\music.wav")
		self.backgroundmusic.start(300, -1)
		
		self.backgroundmenuimage = Image()
		self.backgroundmenuimage.createimage("img\\backgroundmenu\\", "backgroundmenuimage")
		self.backgroundmenupapichimage = Image()
		self.backgroundmenupapichimage.createimage("img\\backgroundmenu\\", "backgroundmenupapich")
		self.backgroundmenublackimage = Image()
		self.backgroundmenublackimage.createimage("img\\backgroundmenu\\", "backgroundmenublack")
		
		self.snowanimation = Animation("img\\snow\\", 29)
		self.snowanimation.loadallimage()
		
		#self.testtext = Text()
		#self.testtext.loadtext("TestText", "times", 24, COLOR.CYAN)
		
		self.startbutton = Button("start")
		self.startbutton.loadbutton("button", "Начать игру", "times", 32, COLOR.BLACK, 2, 1.5)
		self.settingsbutton = Button("settings")
		self.settingsbutton.loadbutton("settings", "", "times", 32, COLOR.BLACK, 1/16, 1/16)
		self.exitbutton = Button("exit")
		self.exitbutton.loadbutton("exit", "", "times", 32, COLOR.BLACK, 1/16, 1/16)
	
	def postInit(self):
		self.backgroundmenuimage.showimage(960, 540)
		self.snowanimation.showanimation(960, 540, 2)
		self.backgroundmenupapichimage.showimage(650, 750)
		self.backgroundmenublackimage.showimage(960, 540)
		self.startbutton.showbutton(1400, 400)
		self.settingsbutton.showbutton(1920 - 10, 0 + 10, "topright")
		self.exitbutton.showbutton(1920 - 10, 1080 - 10, "bottomright")
		self.time+=1