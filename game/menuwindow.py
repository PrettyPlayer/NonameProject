import os
import sys

import pygame

from game.Window import Window
from game.Image import Image
from game.Text import Text
from game.Button import Button
from game.Animation import Animation
from game.Music import Music
from game.Sound import Sound
from game.Colors import Colors, COLOR
from game.Registry import Registry, OPTIONS

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
					self.startButton.click(event.pos)
					self.settingsButton.click(event.pos)
					self.exitButton.click(event.pos)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pass
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
	
	def preInit(self):
		pygame.mixer.music.stop()
		self.time=0
		self.backgroundMusic = Music("music")
		self.backgroundMusic.start(300, -1)
		
		# createStaticImage: posX, posY, pos, name, path=None, sizeX=1, sizeY=1
		# createImage: name, path=None, sizeX=1, sizeY=1
		self.backgroundMenuImage = Image()
		self.backgroundMenuImage.createStaticImage(960, 540, "center", "backgroundmenuimage", "backgroundmenu\\")
		
		self.backgroundMenuPapichImage = Image()
		self.backgroundMenuPapichImage.createStaticImage(650, 750, "center", "backgroundmenupapich", "backgroundmenu\\")
		
		self.backgroundMenuBlackImage = Image()
		self.backgroundMenuBlackImage.createStaticImage(960, 540, "center", "backgroundmenublack", "backgroundmenu\\")
		
		# createStaticAnimation: posX, posY, pos, sizeX=1, sizeY=1
		# createAnimation: sizeX=1, sizeY=1
		self.snowAnimation = Animation("snow\\", 29)
		self.snowAnimation.createStaticAnimation(960, 540, "center")
		
		# createStaticButton: name, posX, posY, pos, text, font, sizeText, color, sizeX=1, sizeY=1
		# createButton: name, text, font, sizeText, color, sizeX=1, sizeY=1
		self.startButton = Button("start")
		self.startButton.createStaticButton("button", 1400, 400, "center", "Начать игру", "times", 32, COLOR.BLACK, 2, 1.5)
		
		self.settingsButton = Button("settings")
		self.settingsButton.createStaticButton("settings", 1920 - 10, 0 + 10, "topright", "", "times", 32, COLOR.BLACK, 1/16, 1/16)
		
		self.exitButton = Button("exit")
		self.exitButton.createStaticButton("exit", 1920 - 10, 1080 - 10, "bottomright", "", "times", 32, COLOR.BLACK, 1/16, 1/16)
	
	def postInit(self):
		# showImage: posX, posY, pos="center"
		# showText: posX, posY
		# showButton: posX, posY, pos="center"
		# showAnimation: posX, posY, speed
		# showStaticAnimation: speed
		self.backgroundMenuImage.showStaticImage()
		self.snowAnimation.showStaticAnimation(2)
		self.backgroundMenuPapichImage.showStaticImage()
		self.backgroundMenuBlackImage.showStaticImage()
		self.startButton.showStaticButton()
		self.settingsButton.showStaticButton()
		self.exitButton.showStaticButton()
		self.time+=1