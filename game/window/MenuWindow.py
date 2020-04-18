import os
import sys

import pygame

from game.window.Window import Window
from game.visual.Image import Image
from game.visual.Text import Text
from game.visual.Button import Button
from game.visual.Animation import Animation
from game.visual.Music import Music
from game.visual.Sound import Sound
from game.visual.Colors import Colors, COLOR
from game.visual.Fog import Fog
from game.system.Registry import Registry, OPTIONS

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
		
		# createStaticImage: posX, posY, pos, name,
		#                    path=None, sizeX=1, sizeY=1
		# createImage: name, path=None, sizeX=1, sizeY=1
		self.backgroundMenuImage = Image()
		self.backgroundMenuImage.createStaticImage(960, 540, "center",
		                    "backgroundmenuimage", "backgroundmenu\\")
		
		#self.backgroundMenuPapichImage = Image()
		#self.backgroundMenuPapichImage.createStaticImage(650-480, 1080, "bottomleft",
		#                         "backgroundmenupapich", "backgroundmenu\\", 1.2, 1.2)
		self.backgroundMenuEpifImage = Image()
		self.backgroundMenuEpifImage.createStaticImage(0, 1080, "bottomleft",
		                         "4", "backgroundmenu\\", 1.8, 1.8)
		
		self.backgroundMenuPahomImage = Image()
		self.backgroundMenuPahomImage.createStaticImage(1750, 800, "bottomright",
		                         "2.1", "backgroundmenu\\", 1.1, 1.1)
		
		self.backgroundMenuBlackImage = Image()
		self.backgroundMenuBlackImage.createStaticImage(960, 540, "center",
		                         "backgroundmenublack", "backgroundmenu\\")
		
		self.fog = Fog()
		self.fog.createImage("fog", "backgroundmenu\\")
		# createStaticAnimation: posX, posY, pos, sizeX=1, sizeY=1
		# createAnimation: sizeX=1, sizeY=1
		#self.snowAnimation = Animation("snow\\", 240)
		#self.snowAnimation.createStaticAnimation(960, 540, "center", 2.5, 2.5)
		
		# createStaticButton: name, posX, posY, pos, text, font,
		#                     sizeText, color, sizeX=1, sizeY=1
		# createButton: name, text, font, sizeText,
		#               color, sizeX=1, sizeY=1
		self.startButton = Button("start")
		self.startButton.createStaticButton("button", OPTIONS.getReg("width")/2, 980, "center",
		                  "Начать игру", "times", 32, COLOR.BLACK, 2, 1.5)
		
		self.settingsButton = Button("settings")
		self.settingsButton.createStaticButton("settings", 1920 - 10, 0 + 10,
		                "topright", "", "times", 32, COLOR.BLACK, 1/16, 1/16)
		
		self.exitButton = Button("exit")
		self.exitButton.createStaticButton("exit", 1920 - 10, 1080 - 10,
		        "bottomright", "", "times", 32, COLOR.BLACK, 1/16, 1/16)
		
		self.backgroundMusic = Music("music")
		self.backgroundMusic.start(300, -1)
	def postInit(self):
		# showImage: posX, posY, pos="center"
		# showText: posX, posY
		# showButton: posX, posY, pos="center"
		# showAnimation: posX, posY, speed
		# showStaticAnimation: speed
		self.backgroundMenuImage.showStaticImage()
		self.fog.changePos(4)
		self.fog.showImage(self.fog.posX, self.fog.posY, "topleft")
		#self.snowAnimation.showStaticAnimation(1)
		#self.backgroundMenuPapichImage.showStaticImage()
		self.backgroundMenuPahomImage.showStaticImage()
		self.backgroundMenuEpifImage.showStaticImage()
		#self.backgroundMenuBlackImage.showStaticImage()
		self.startButton.showStaticButton()
		self.settingsButton.showStaticButton()
		self.exitButton.showStaticButton()
		self.time+=1