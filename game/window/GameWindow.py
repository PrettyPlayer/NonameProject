import os
import sys
import math

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
					if self.navigationNum == 1:
						if self.numSfx < 2:
							self.numSfx += 1
							self.flagSfx = 1
					elif self.navigationNum == 2:
						self.volumeSnd = self.snd[1].get_volume()*100
						if self.volumeSnd < 100:
							self.volumeSnd += 10
							self.flagSfx = 1
						self.volumeSnd = math.ceil(self.volumeSnd)
				if event.key == pygame.K_DOWN:
					if self.navigationNum == 1:
						if 1 < self.numSfx:
							self.numSfx -= 1
							self.flagSfx = 1
					elif self.navigationNum == 2:
						self.volumeSnd = self.snd[1].get_volume()*100
						if 0 < self.volumeSnd:
							self.volumeSnd -= 10
							self.flagSfx = 1
						self.volumeSnd = math.ceil(self.volumeSnd)
				if event.key == pygame.K_LEFT:
					if 1 < self.navigationNum:
						self.navigationNum -= 1
				if event.key == pygame.K_RIGHT:
					if self.navigationNum < 2:
						self.navigationNum += 1
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
				if event.key in self.eventKeyDict.keys():
					self.snd[self.eventKeyDict[event.key]].play()
					self.isPressedKeyDict[self.eventKeyDict[event.key]] = 1
			elif event.type == pygame.KEYUP:
				if event.key in self.eventKeyDict.keys():
					self.isPressedKeyDict[self.eventKeyDict[event.key]] = 0
					
				print(event.key)
	def preInit(self):
		pygame.mixer.music.stop()
		self.backgroundGameImage = Image()
		self.backgroundGameImage.createStaticImage(960, 540, "center", "backgroundgameimage", "backgroundgame\\")
		self.pianoImage = Image()
		self.pianoImage.createStaticImage(960, 1080, "bottom", "Piano", "backgroundgame\\")
		self.imgPressedKey = {}
		
		self.navigationNum = 1
		self.numSfx = 1
		self.flagSfx = 1
		self.snd = {}
		self.volumeSnd = 100
		self.textWhite = {}
		self.textBlack = {}
		self.dirPosBlackText = {12: 0, 13: 99, 14: 151, 15: 101, 16: 151, 17: 99, 18: 100, 19: 150, 20: 103}
		self.textSfx = Text()
		self.textSfx.createText("text", "times", 36, COLOR.BLACK)
		self.textCurrentSamples = Text()
		self.textCurrentSamples.createStaticText("Samples:", "times", 36, COLOR.BLACK, 200, 200)
		self.textVolume = Text()
		self.textVolume.createText("text", "times", 36, COLOR.BLACK)
		self.textCurrentVolume = Text()
		self.textCurrentVolume.createStaticText("Volume:", "times", 36, COLOR.BLACK, 400, 200)
		#self.startPosText = 530
		self.startPosText = self.pianoImage.rect[0] + 72
		self.changePosText = 0
		self.isPressedKeyDict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
		self.imgPressedKeyDict = {1: "6", 2: "7", 3: "1", 4: "2", 5: "3", 6: "4", 7: "5", 8: "6", 9: "7", 10: "1", 11: "2", 12: "black", 13: "black", 14: "black", 15: "black", 16: "black", 17: "black", 18: "black", 19: "black", 20: "black"}
		#self.imgPressedKeyDict = {1: "black", 2: "6", 3: "black", 4: "7", 5: "1", 6: "black", 7: "2", 8: "black", 9: "3", 10: "4", 11: "black", 12: "5", 13: "black", 14: "6", 15: "black", 16: "7", 17: "1", 18: "black", 19: "2", 20: "black"}
		self.widthPressedKeyDict = {1: 69, 2: 155, 3: 242, 4: 327, 5: 413, 6: 499, 7: 585, 8: 670, 9: 756, 10: 842, 11: 927, 12: 26, 13: 125, 14: 277, 15: 379, 16: 530, 17: 627, 18: 726, 19: 877, 20: 979}
		self.textDict = {1: "A", 2: "S", 3: "D", 4: "F", 5: "G", 6: "H", 7: "J", 8: "K", 9: "L", 10: "Ж", 11: "Э", 12: "Q", 13: "W", 14: "R", 15: "T", 16: "U", 17: "I", 18: "O", 19: "[", 20: "]"}
		self.eventKeyDict = {113: 12, 97: 1, 119: 13, 115: 2, 100: 3, 114: 14, 102: 4, 116: 15, 103: 5, 104: 6, 117: 16, 106: 7, 105: 17, 107: 8, 111: 18, 108: 9, 59: 10, 91: 19, 39: 11, 93: 20}
		
		for i in range(1, 12):
			self.imgPressedKey[i] = Image()
			self.imgPressedKey[i].createStaticImage(self.pianoImage.rect[0] + self.widthPressedKeyDict[i], self.pianoImage.rect[1] + 224, "center", self.imgPressedKeyDict[i], "piano\\")
		for i in range(12, 21):
			self.imgPressedKey[i] = Image()
			self.imgPressedKey[i].createStaticImage(self.pianoImage.rect[0] + self.widthPressedKeyDict[i], self.pianoImage.rect[1] + 149, "center", self.imgPressedKeyDict[i], "piano\\")
		
		for i in range(1, 12):
			self.textWhite[i] = Text()
			self.textWhite[i].createStaticText(self.textDict[i], "times", 24, COLOR.BLACK, self.startPosText + self.changePosText, self.pianoImage.rect[1] + 400)
			self.changePosText += 86
		#self.startPosText = 484
		self.startPosText = self.pianoImage.rect[0] + 72 - 46
		self.changePosText = 0
		for i in range(12, 21):
			self.changePosText += self.dirPosBlackText[i]
			self.textBlack[i] = Text()
			self.textBlack[i].createStaticText(self.textDict[i], "times", 24, COLOR.WHITE, self.startPosText + self.changePosText, self.pianoImage.rect[1] + 256)
	def postInit(self):
		if self.flagSfx:
			if self.numSfx == 1:
				self.sfx = "fork"
			elif self.numSfx == 2:
				self.sfx = "oh"
			for i in range(1, 21):
				self.snd[i] = pygame.mixer.Sound("sfx\\" + self.sfx + "\\" + str(i) + ".wav")
				self.snd[i].set_volume(self.volumeSnd/100)
			self.textSfx.createText(self.sfx, "times", 36, COLOR.BLACK)
			self.textVolume.createText(self.volumeSnd, "times", 36, COLOR.BLACK)
		
		self.backgroundGameImage.showStaticImage()
		self.pianoImage.showStaticImage()
		self.textCurrentSamples.showStaticText()
		self.textCurrentVolume.showStaticText()
		self.textSfx.showText(200, 250)
		self.textVolume.showText(400, 250)
		for i in range(1, 21):
			if self.isPressedKeyDict[i] == 1:
				self.imgPressedKey[i].showStaticImage()
		
		for i in range(1, 12):
			self.textWhite[i].showStaticText()
		for i in range(12, 21):
			self.textBlack[i].showStaticText()