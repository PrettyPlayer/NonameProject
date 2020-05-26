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
			#Выход на крестик
			if event.type == pygame.QUIT:
				self.exit()
				
			#Отпускание клавиши
			elif event.type == pygame.KEYUP:
				#Остановка звука при отжатии клавиши (Если self.fadeSnd = 1)
				if event.key in self.eventKeyDict.keys() and self.isPressedKeyDict[self.eventKeyDict[event.key]] == 1 and self.fadeSnd == 1:
					self.snd[self.eventKeyDict[event.key]].stopSnd()
					self.isPressedKeyDict[self.eventKeyDict[event.key]] = 0
			
			#Нажатие клавиши
			elif event.type == pygame.KEYDOWN:
				#Игра во весь экран
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
				#Звук на нажатие клавиши синтезатора
				if event.key in self.eventKeyDict.keys():
					print("Нажата клавиша", event.key)
					self.snd[self.eventKeyDict[event.key]].playSnd()
					self.isPressedKeyDict[self.eventKeyDict[event.key]] = 1
				#Изменение пункта меню (Вверх)
				elif event.key == pygame.K_UP:
					if self.numNavigation == 1:
						#Выбор инструмента (Вверх)
						if self.numInstrument < 5:
							self.numInstrument += 1
							self.isChangeInstrumentSfx = 1
					elif self.numNavigation == 2:
						#Изменение громкости (Вверх)
						self.volumeSnd = self.snd[1].sound.get_volume()*100
						if self.volumeSnd < 100:
							self.volumeSnd += 10
							self.isChangeVolumeSfx = 1
						self.volumeSnd = math.ceil(self.volumeSnd)
					elif self.numNavigation == 3:
						#Выбор нот (Вверх)
						if self.numNotes <1:
							self.numNotes += 1
							self.isChangeNotes = 1
				#Изменение пункта меню (Вниз)
				elif event.key == pygame.K_DOWN:
					if self.numNavigation == 1:
						#Выбор инструмента (Вниз)
						if 1 < self.numInstrument:
							self.numInstrument -= 1
							self.isChangeInstrumentSfx = 1
					elif self.numNavigation == 2:
						#Изменение громкости (Вниз)
						self.volumeSnd = self.snd[1].sound.get_volume()*100
						if 0 < self.volumeSnd:
							self.volumeSnd -= 10
							self.isChangeVolumeSfx = 1
						self.volumeSnd = math.ceil(self.volumeSnd)
					elif self.numNavigation == 3:
						#Выбор нот (Вниз)
						if 1 < self.numNotes:
							self.numNotes -= 1
							self.isChangeNotes = 1
				#Перемещение в меню (Вправо)
				elif event.key == pygame.K_RIGHT:
					if self.numNavigation < 3:
						self.numNavigation += 1
				#Перемещение в меню (Влево)
				elif event.key == pygame.K_LEFT:
					if 1 < self.numNavigation:
						self.numNavigation -= 1
			
	def preInit(self):
		#Создание переменных/словарей
		self.numNavigation = 1
		self.numInstrument = 1
		self.fadeSnd = 0
		self.volumeSnd = 100
		self.numNotes = 1
		self.isChangeInstrumentSfx = 1
		self.isChangeVolumeSfx = 1
		self.isChangeNotes = 1
		self.snd = {}
		self.textWhite = {}
		self.textBlack = {}
		
		#Заполнение словарей
		self.dirPosBlackText = {12: 0, 13: 99, 14: 151, 15: 101, 16: 151, 17: 99, 18: 100, 19: 150, 20: 103}
		self.isPressedKeyDict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
		self.imgPressedKeyDict = {1: "6", 2: "7", 3: "1", 4: "2", 5: "3", 6: "4", 7: "5", 8: "6", 9: "7", 10: "1", 11: "2", 12: "black", 13: "black", 14: "black", 15: "black", 16: "black", 17: "black", 18: "black", 19: "black", 20: "black"}
		self.widthPressedKeyDict = {1: 69, 2: 155, 3: 242, 4: 327, 5: 413, 6: 499, 7: 585, 8: 670, 9: 756, 10: 842, 11: 927, 12: 26, 13: 125, 14: 277, 15: 379, 16: 530, 17: 627, 18: 726, 19: 877, 20: 979}
		self.textDict = {1: "A", 2: "S", 3: "D", 4: "F", 5: "G", 6: "H", 7: "J", 8: "K", 9: "L", 10: "Ж", 11: "Э", 12: "Q", 13: "W", 14: "R", 15: "T", 16: "U", 17: "I", 18: "O", 19: "[", 20: "]"}
		self.eventKeyDict = {113: 12, 97: 1, 119: 13, 115: 2, 100: 3, 114: 14, 102: 4, 116: 15, 103: 5, 104: 6, 117: 16, 106: 7, 105: 17, 107: 8, 111: 18, 108: 9, 59: 10, 91: 19, 39: 11, 93: 20}
		
		#Остановка музыки из предыдущего окна (MenuWindow)
		pygame.mixer.music.stop()
		
		#Создание переменных с изображениями
		self.backgroundGameImage = Image()
		self.backgroundGameImage.createStaticImage(960, 540, "center", "backgroundgameimage", "backgroundgame\\")
		self.pianoImage = Image()
		self.pianoImage.createStaticImage(960, 1080, "bottom", "Piano", "backgroundgame\\")
		self.imgPressedKey = {}
		self.volumeFrame = Image()
		self.volumeFrame.createStaticImage(1700, 600, "center", "volumeFrame", "options\\")
		self.volumeFill = Image()
		self.volumeFill.createImage("volumeFill", "options\\")
		
		#Создание переменных с текстом
		self.textSamples = Text()
		self.textSamples.createStaticText("Samples:", "times", 36, COLOR.BLACK, 200, 200)
		self.textVolume = Text()
		self.textVolume.createStaticText("Volume:", "times", 36, COLOR.BLACK, 200, 400)
		self.textNotes = Text()
		self.textNotes.createStaticText("Notes:", "times", 36, COLOR.BLACK, 200, 600)
		self.textCurrentSamples = Text()
		self.textCurrentSamples.createText("text", "times", 36, COLOR.BLACK)
		self.textCurrentVolume = Text()
		self.textCurrentVolume.createText("text", "times", 36, COLOR.BLACK)
		self.textCurrentNotes = Text()
		self.textCurrentNotes.createText("text", "times", 36, COLOR.BLACK)
		
		#Создание словарей изображений
		for i in range(1, 12):
			self.imgPressedKey[i] = Image()
			self.imgPressedKey[i].createStaticImage(self.pianoImage.rect[0] + self.widthPressedKeyDict[i], self.pianoImage.rect[1] + 224, "center", self.imgPressedKeyDict[i], "piano\\")
		for i in range(12, 21):
			self.imgPressedKey[i] = Image()
			self.imgPressedKey[i].createStaticImage(self.pianoImage.rect[0] + self.widthPressedKeyDict[i], self.pianoImage.rect[1] + 149, "center", self.imgPressedKeyDict[i], "piano\\")
		
		#Создание словарей текста
		#self.startPosText = 530
		self.startPosText = self.pianoImage.rect[0] + 72
		self.changePosText = 0
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
		#Области
		self.volumeFillSurface = pygame.Surface((200, 200))
		self.volumeFillSurface.set_colorkey((0, 0, 0))
		
		#Изменения меню
		if self.isChangeInstrumentSfx:
			if self.numInstrument == 1:
				self.sfx = "Grand Piano"
			elif self.numInstrument == 2:
				self.sfx = "Flute"
			elif self.numInstrument == 3:
				self.sfx = "Flute Attack"
			elif self.numInstrument == 4:
				self.sfx = "fork"
			elif self.numInstrument == 5:
				self.sfx = "oh"
			self.textCurrentSamples.createText(self.sfx, "times", 36, COLOR.BLACK)
			self.isChangeInstrumentSfx = 0
		
		#Изменение громкости
		if self.isChangeVolumeSfx:
			for i in range(1, 21):
				self.snd[i] = Sound(str(i), self.sfx)
				self.snd[i].setVolume(self.volumeSnd)
			self.textCurrentVolume.createText(self.volumeSnd, "times", 36, COLOR.BLACK)
			self.isChangeVolumeSfx = 0
		
		#Изменение нот
		if self.isChangeNotes:
			if self.numNotes == 1:
				self.notes = "Samidare"
			self.textCurrentNotes.createText(self.notes, "times", 36, COLOR.BLACK)
			self.isChangeNotes = 0
		
		#Отрисовка изображений/текста
		self.backgroundGameImage.showStaticImage()
		self.pianoImage.showStaticImage()
		self.textSamples.showStaticText()
		self.textVolume.showStaticText()
		self.textNotes.showStaticText()
		self.textCurrentSamples.showText(200, 250)
		self.textCurrentVolume.showText(200, 450)
		self.textCurrentNotes.showText(200, 650)
		
		self.volumeFill.changeRectImage(0, (100-self.volumeSnd)*2, "topleft")
		self.volumeFillSurface.blit(self.volumeFill.image, self.volumeFill.rect)
		OPTIONS.getReg("surf_main").blit(self.volumeFillSurface, (1600, 500))
		self.volumeFrame.showStaticImage()
		
		#Проверка на отжатие клавиши и её отрисовка
		for i in range(1, 21):
			print(self.snd[i].sound)
			if self.snd[i].sound.get_num_channels() < 0:
				self.isPressedKeyDict[self.eventKeyDict[event.key]] = 0
				if self.isPressedKeyDict[i] == 1:
					self.imgPressedKey[i].showStaticImage()
		
		for i in range(1, 12):
			self.textWhite[i].showStaticText()
		for i in range(12, 21):
			self.textBlack[i].showStaticText()
			
		pygame.display.update()