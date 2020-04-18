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
from game.object.Papich import Papich
from game.system.Registry import Registry, OPTIONS

class GameWindow(Window):
	def __init__(self):
		self.scene = 1
		self.run = True
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT):
					self.papich.changePos(event.key)
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
				if event.key == pygame.K_q:
					self.snd1.play()
				if event.key == pygame.K_a:
					self.snd2.play()
				if event.key == pygame.K_w:
					self.snd3.play()
				if event.key == pygame.K_s:
					self.snd4.play()
				if event.key == pygame.K_d:
					self.snd5.play()
				if event.key == pygame.K_r:
					self.snd6.play()
				if event.key == pygame.K_f:
					self.snd7.play()
				if event.key == pygame.K_t:
					self.snd8.play()
				if event.key == pygame.K_g:
					self.snd9.play()
				if event.key == pygame.K_h:
					self.snd10.play()
				if event.key == pygame.K_u:
					self.snd11.play()
				if event.key == pygame.K_j:
					self.snd12.play()
				if event.key == pygame.K_i:
					self.snd13.play()
				if event.key == pygame.K_k:
					self.snd14.play()
				if event.key == pygame.K_o:
					self.snd15.play()
				if event.key == pygame.K_l:
					self.snd16.play()
				if event.key == pygame.K_SEMICOLON:
					self.snd17.play()
				if event.key == pygame.K_LEFTBRACKET:
					self.snd18.play()
				if event.key == pygame.K_QUOTE:
					self.snd19.play()
				if event.key == pygame.K_RIGHTBRACKET:
					self.snd20.play()
	
	def preInit(self):
		pygame.mixer.music.stop()
		self.backgroundMenuImage = Image()
		self.backgroundMenuImage.createStaticImage(960, 540, "center",
		                    "backgroundgameimage", "backgroundgame\\")
		self.papich = Papich()
		self.papich.createPapich(960, 380, 1/4, 1/4)
		self.sfx = "fork"
		self.snd1 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\1.wav")
		self.snd2 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\2.wav")
		self.snd3 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\3.wav")
		self.snd4 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\4.wav")
		self.snd5 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\5.wav")
		self.snd6 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\6.wav")
		self.snd7 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\7.wav")
		self.snd8 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\8.wav")
		self.snd9 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\9.wav")
		self.snd10 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\10.wav")
		self.snd11 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\11.wav")
		self.snd12 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\12.wav")
		self.snd13 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\13.wav")
		self.snd14 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\14.wav")
		self.snd15 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\15.wav")
		self.snd16 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\16.wav")
		self.snd17 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\17.wav")
		self.snd18 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\18.wav")
		self.snd19 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\19.wav")
		self.snd20 = pygame.mixer.Sound("sfx\\" + self.sfx + "\\20.wav")
	def postInit(self):
		self.backgroundMenuImage.showStaticImage()
		self.papich.showPapich()
	
