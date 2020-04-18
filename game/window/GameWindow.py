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
				if event.key == pygame.K_UP:
					if self.numSfx < 2:
						self.numSfx += 1
						self.flagSfx = 1
				if event.key == pygame.K_DOWN:
					if 1 < self.numSfx:
						self.numSfx -= 1
						self.flagSfx = 1
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
				if event.key == pygame.K_q:
					self.snd[1].play()
				if event.key == pygame.K_a:
					self.snd[2].play()
				if event.key == pygame.K_w:
					self.snd[3].play()
				if event.key == pygame.K_s:
					self.snd[4].play()
				if event.key == pygame.K_d:
					self.snd[5].play()
				if event.key == pygame.K_r:
					self.snd[6].play()
				if event.key == pygame.K_f:
					self.snd[7].play()
				if event.key == pygame.K_t:
					self.snd[8].play()
				if event.key == pygame.K_g:
					self.snd[9].play()
				if event.key == pygame.K_h:
					self.snd[10].play()
				if event.key == pygame.K_u:
					self.snd[11].play()
				if event.key == pygame.K_j:
					self.snd[12].play()
				if event.key == pygame.K_i:
					self.snd[13].play()
				if event.key == pygame.K_k:
					self.snd[14].play()
				if event.key == pygame.K_o:
					self.snd[15].play()
				if event.key == pygame.K_l:
					self.snd[16].play()
				if event.key == pygame.K_SEMICOLON:
					self.snd[17].play()
				if event.key == pygame.K_LEFTBRACKET:
					self.snd[18].play()
				if event.key == pygame.K_QUOTE:
					self.snd[19].play()
				if event.key == pygame.K_RIGHTBRACKET:
					self.snd[20].play()
	def preInit(self):
		pygame.mixer.music.stop()
		self.backgroundGameImage = Image()
		self.backgroundGameImage.createStaticImage(960, 540, "center", "backgroundgameimage", "backgroundgame\\")
		self.pianoImage = Image()
		self.pianoImage.createStaticImage(960, 540, "center", "Piano", "backgroundgame\\")
		self.numSfx = 1
		self.flagSfx = 1
		self.snd = {}
		self.text = {}
		self.startPosText = 530
		self.changePosText = 0
		for i in range(1, 12):
			self.text[i] = Text()
			self.text[i].createStaticText(str(i), "times", 24, COLOR.BLACK, self.startPosText + self.changePosText, 700)
			self.changePosText += 86
	def postInit(self):
		if self.flagSfx:
			if self.numSfx == 1:
				self.sfx = "fork"
			if self.numSfx == 2:
				self.sfx = "oh"
			for i in range(1, 21):
				self.snd[i] = pygame.mixer.Sound("sfx\\" + self.sfx + "\\" + str(i) + ".wav")
		self.backgroundGameImage.showStaticImage()
		self.pianoImage.showStaticImage()
		for i in range(1, 12):
			self.text[i].showStaticText()