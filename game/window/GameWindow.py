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
			
			#Нажатие клавиши
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LSHIFT:
					self.fadeSnd = 0
				if event.key == pygame.K_SPACE:
					self.isChangeNotesPage = 1
				#Игра во весь экран
				if event.key == pygame.K_RETURN:
					self.changeFullscreen()
				#Звук на нажатие клавиши ударных
				if 256 < event.key < 266:
					self.sndDrum[event.key-256].playSnd()
					self.isPressedKeyDictDrum[event.key-256] = 1
				#Звук на нажатие клавиши синтезатора
				if event.key in self.eventKeyDict.keys():
					self.snd[self.eventKeyDict[event.key]].playSnd()
					self.isPressedKeyDict[self.eventKeyDict[event.key]] = 1
				#Изменение пункта меню (Вверх)
				if event.key == pygame.K_UP:
					if self.numNavigation == 1:
						#Выбор инструмента (Вверх)
						if self.numInstrument < 5:
							self.numInstrument += 1
							self.isChangeInstrument = 1
					elif self.numNavigation == 2:
						#Изменение громкости (Вверх)
						self.volumeSnd = self.snd[1].sound.get_volume()*100
						if self.volumeSnd < 100:
							self.volumeSnd += 10
							self.isChangeVolumeSfx = 1
						self.volumeSnd = math.ceil(self.volumeSnd)
					elif self.numNavigation == 3:
						#Изменение fade
						if self.strFade < 2000:
							self.strFade += 100
							self.isChangeStrFade = 1
					elif self.numNavigation == 4:
						#Выбор нот (Вверх)
						if self.numNotes < 1:
							self.numNotes += 1
							self.isChangeNotes = 1
				#Изменение пункта меню (Вниз)
				elif event.key == pygame.K_DOWN:
					if self.numNavigation == 1:
						#Выбор инструмента (Вниз)
						if 1 < self.numInstrument:
							self.numInstrument -= 1
							self.isChangeInstrument = 1
					elif self.numNavigation == 2:
						#Изменение громкости (Вниз)
						self.volumeSnd = self.snd[1].sound.get_volume()*100
						if 0 < self.volumeSnd:
							self.volumeSnd -= 10
							self.isChangeVolumeSfx = 1
						self.volumeSnd = math.ceil(self.volumeSnd)
					elif self.numNavigation == 3:
						#Изменение fade
						if 0 < self.strFade:
							self.strFade -= 100
							self.isChangeStrFade = 1
					elif self.numNavigation == 4:
						#Выбор нот (Вниз)
						if 0 < self.numNotes:
							self.numNotes -= 1
							self.isChangeNotes = 1
				#Перемещение в меню (Вправо)
				elif event.key == pygame.K_RIGHT:
					if self.numNavigation < 4:
						self.numNavigation += 1
				#Перемещение в меню (Влево)
				elif event.key == pygame.K_LEFT:
					if 1 < self.numNavigation:
						self.numNavigation -= 1
			
			#Отпускание клавиши
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LSHIFT:
					self.fadeSnd = 1
				#Остановка звука при отжатии клавиши (Если self.fadeSnd = 1)
				if event.key in self.eventKeyDict.keys():
					if self.isPressedKeyDict[self.eventKeyDict[event.key]] == 1 and self.fadeSnd == 1:
						self.snd[self.eventKeyDict[event.key]].stopSnd(self.strFade)
						self.isPressedKeyDict[self.eventKeyDict[event.key]] = 0
				if 256 < event.key < 266:
					self.isPressedKeyDictDrum[event.key-256] = 0
			
	def preInit(self):
		#Создание переменных/словарей
		self.numNavigation = 1
		self.numInstrument = 1
		self.fadeSnd = 1
		self.strFade = 100
		self.volumeSnd = 100
		self.numNotes = 0
		self.isChangeInstrument = 1
		self.isChangeVolumeSfx = 1
		self.isChangeStrFade = 1
		self.isChangeNotes = 1
		self.pianoScale = 0.648
		self.snd = {}
		self.sndDrum = {}
		self.textWhite = {}
		self.textBlack = {}
		
		#Заполнение словарей
		self.pagesOfNotes = {1: 5}
		self.dirPosBlackText = {12: 0, 13: 100, 14: 153, 15: 101, 16: 151, 17: 97, 18: 98, 19: 150, 20: 103}
		self.isPressedKeyDict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
		self.isPressedKeyDictDrum = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
		self.imgPressedKeyDict = {1: "6", 2: "7", 3: "1", 4: "2", 5: "3", 6: "4", 7: "5", 8: "6", 9: "7", 10: "1", 11: "2", 12: "black", 13: "black", 14: "black", 15: "black", 16: "black", 17: "black", 18: "black", 19: "black", 20: "black"}
		#self.widthPressedKeyDict = {1: 69, 2: 155, 3: 242, 4: 327, 5: 413, 6: 499, 7: 585, 8: 670, 9: 756, 10: 842, 11: 927, 12: 26, 13: 125, 14: 277, 15: 379, 16: 530, 17: 627, 18: 726, 19: 877, 20: 979}
		self.widthPressedKeyDict = {1: 69, 2: 155, 3: 241, 4: 327, 5: 412, 6: 499, 7: 584, 8: 670, 9: 755, 10: 841, 11: 927, 12: 26, 13: 125, 14: 278, 15: 379, 16: 530, 17: 627, 18: 726, 19: 877, 20: 979}
		self.textDict = {1: "A", 2: "S", 3: "D", 4: "F", 5: "G", 6: "H", 7: "J", 8: "K", 9: "L", 10: "Ж", 11: "Э", 12: "Q", 13: "W", 14: "R", 15: "T", 16: "U", 17: "I", 18: "O", 19: "[", 20: "]"}
		self.eventKeyDict = {113: 12, 97: 1, 119: 13, 115: 2, 100: 3, 114: 14, 102: 4, 116: 15, 103: 5, 104: 6, 117: 16, 106: 7, 105: 17, 107: 8, 111: 18, 108: 9, 59: 10, 91: 19, 39: 11, 93: 20}
		
		#Остановка музыки из предыдущего окна (MenuWindow)
		pygame.mixer.music.stop()
		
		#Создание переменных с изображениями
		self.backgroundGameImage = Image()
		#self.backgroundGameImage.createStaticImage(960, 540, "center", "backgroundgameimage", "backgroundgame")
		self.backgroundGameImage.createStaticImage(960, 540, "center", "backgroundgameimage2", "backgroundgame")
		self.pianoImage = Image()
		#self.pianoImage.createStaticImage(960, 1080, "bottom", "Piano", "backgroundgame")
		self.pianoImage.createStaticImage(960, 1075, "bottom", "Piano3", "piano")
		self.drumImage = Image()
		self.drumImage.createStaticImage(self.pianoImage.rect[0] + 846, self.pianoImage.rect[1] + 355, "center", "drumBlue", "drum")
		self.imgPressedKey = {}
		self.imgPressedKeyDrum = {}
		
		self.frameImage = Image()
		self.frameImage.createImage("frameRed", "options")
		self.instrumentImage = Image()
		self.instrumentImage.createStaticImage(494+78, 573+78, "center", "Grand Piano", "instruments")
		self.fadeFrame = Image()
		self.fadeFrame.createStaticImage(494+78+204+204, 573+78, "center", "frameBlack", "options")
		self.volumeFrame = Image()
		self.volumeFrame.createStaticImage(494+78+204, 573+78, "center", "volumeFrame", "options")
		self.notesFrameImage = Image()
		self.notesFrameImage.createStaticImage(494+78, 573+78, "center", "None", "None", "notes")
		
		self.volumeFill = Image()
		self.volumeFill.createImage("volumeFill", "options")
		self.fadeFill = Image()
		self.fadeFill.createImage("volumeFill", "options")
		
		#Создание переменных с текстом
		#self.textSamples = Text()
		#self.textSamples.createStaticText("Samples:", "times", 36, COLOR.BLACK, 200, 200)
		#self.textVolume = Text()
		#self.textVolume.createStaticText("Volume:", "times", 36, COLOR.BLACK, 200, 400)
		self.textStrFade = Text()
		self.textStrFade.createStaticText("Fade-out:", "times", 30, COLOR.DARKRED, 494+78+204+204, 573+60)
		self.textNotes = Text()
		self.textNotes.createStaticText("Notes:", "times", 36, COLOR.BLACK, 200, 800)
		#self.textCurrentSamples = Text()
		#self.textCurrentSamples.createText("text", "times", 36, COLOR.BLACK)
		#self.textCurrentVolume = Text()
		#self.textCurrentVolume.createText("text", "times", 36, COLOR.BLACK)
		self.textCurrentStrFade = Text()
		self.textCurrentStrFade.createText("text", "times", 24, COLOR.BLACK)
		self.textCurrentNotes = Text()
		self.textCurrentNotes.createText("text", "times", 36, COLOR.BLACK)
		
		#Создание словарей изображений
		for i in range(1, 12):
			self.imgPressedKey[i] = Image()
			self.imgPressedKey[i].createStaticImage(self.pianoImage.rect[0] + self.widthPressedKeyDict[i] * self.pianoScale + 31, self.pianoImage.rect[1] + 361, "center", self.imgPressedKeyDict[i], "piano")
		for i in range(12, 21):
			self.imgPressedKey[i] = Image()
			self.imgPressedKey[i].createStaticImage(self.pianoImage.rect[0] + self.widthPressedKeyDict[i] * self.pianoScale + 30, self.pianoImage.rect[1] + 312, "center", self.imgPressedKeyDict[i], "piano")
		self.changeWidthDrum = 12
		self.sizeDrumImage = 85
		#Красные квадраты на синих
		z = 1
		for i in range(2, -1, -1):
			for j in range(0, 3):
				self.imgPressedKeyDrum[z] = Image()
				self.imgPressedKeyDrum[z].createStaticImage(self.drumImage.rect[0] + self.sizeDrumImage * j + self.changeWidthDrum * j, self.drumImage.rect[1] + self.sizeDrumImage * i + self.changeWidthDrum * i, "topleft", "drum", "drum")
				z+=1
		
		#Создание словарей текста
		#self.startPosText = 530
		self.startPosText = self.pianoImage.rect[0] + 76
		self.changePosText = 0
		for i in range(1, 12):
			self.textWhite[i] = Text()
			self.textWhite[i].createStaticText(self.textDict[i], "times", 24, COLOR.BLACK, self.startPosText + self.changePosText * self.pianoScale, self.pianoImage.rect[1] + 480)
			self.changePosText += 86
		#self.startPosText = 484
		self.startPosText = self.pianoImage.rect[0] + 72 - 46 + 20
		self.changePosText = 0
		for i in range(12, 21):
			self.changePosText += self.dirPosBlackText[i]
			self.textBlack[i] = Text()
			self.textBlack[i].createStaticText(self.textDict[i], "times", 24, COLOR.WHITE, self.startPosText + self.changePosText * self.pianoScale, self.pianoImage.rect[1] + 390)
		
		#Загрузка звуков ударных
		for i in range(1, 10):
			self.sndDrum[i] = Sound(str(i), "Drum")
			self.sndDrum[i].setVolume(self.volumeSnd)
		
	def postInit(self):
		#Области
		self.volumeFillSurface = pygame.Surface((146, 146))
		self.volumeFillSurface.set_colorkey((0, 0, 0))
		self.fadeFillSurface = pygame.Surface((146, 146))
		self.fadeFillSurface.set_colorkey((0, 0, 0))
		
		#Изменения меню
		if self.isChangeInstrument:
			if self.numInstrument == 1:
				self.sfx = "Grand Piano"
			elif self.numInstrument == 2:
				self.sfx = "Flute"
			elif self.numInstrument == 3:
				self.sfx = "Contrabass"
			elif self.numInstrument == 4:
				self.sfx = "fork"
			elif self.numInstrument == 5:
				self.sfx = "oh"
			for i in range(1, 21):
				self.snd[i] = Sound(str(i), self.sfx)
				self.snd[i].setVolume(self.volumeSnd)
			self.instrumentImage.createStaticImage(494+78, 573+78, "center", self.sfx, "instruments")
			#self.textCurrentSamples.createText(self.sfx, "times", 36, COLOR.BLACK)
			self.isChangeInstrument = 0
		
		#Изменение громкости
		if self.isChangeVolumeSfx:
			for i in range(1, 21):
				self.snd[i].setVolume(self.volumeSnd)
			#self.textCurrentVolume.createText(self.volumeSnd, "times", 36, COLOR.BLACK)
			for i in range(1, 10):
				self.sndDrum[i].setVolume(self.volumeSnd)
			self.isChangeVolumeSfx = 0
		
		#Изменение fade
		if self.isChangeStrFade:
			self.textCurrentStrFade.createText(self.strFade, "times", 30, COLOR.DARKRED)
			self.isChangeStrFade = 0
		
		#Изменение нот
		if self.isChangeNotes:
			if self.numNotes == 0:
				self.notes = "None"
				self.isShowNotesPage = 0
			else:
				if self.numNotes == 1:
					self.notes = "Samidare"
				self.numNotesPage = 1
				self.notesImage = Image()
				#self.notesImage.createStaticImage(960, 47, "top", str(self.numNotesPage), self.notes, "notes")
				self.notesImage.createStaticImage(960, 5, "top", str(self.numNotesPage), self.notes, "notes")
				self.isShowNotesPage = 1
			self.notesFrameImage.createStaticImage(494+78+204+204+204, 573+78, "center", self.notes, self.notes, "notes")
			self.textCurrentNotes.createText(self.notes, "times", 24, COLOR.BLACK)
			self.isChangeNotes = 0
			self.isChangeNotesPage = 0
		
		#Изменение страницы ноты
		if self.isChangeNotesPage and self.numNotes != 0:
			if self.numNotesPage < self.pagesOfNotes[self.numNotes]:
				self.numNotesPage += 1
				#self.notesImage.createStaticImage(960, 47, "top", str(self.numNotesPage), self.notes, "notes")
				self.notesImage.createStaticImage(960, 5, "top", str(self.numNotesPage), self.notes, "notes")
				self.isChangeNotesPage = 0
		
		#Изменение положения фрейма
		self.frameImage.changeRectImage(494+78 + 204*(self.numNavigation-1), 573+78, pos="center")
		
		#Отрисовка изображений/текста
		self.backgroundGameImage.showStaticImage()
		if self.isShowNotesPage:
			self.notesImage.showStaticImage()
		self.pianoImage.showStaticImage()
		self.drumImage.showStaticImage()
		
		self.volumeFill.changeRectImage(0, (100-self.volumeSnd)*1.5, "topleft")
		self.volumeFillSurface.blit(self.volumeFill.image, self.volumeFill.rect)
		self.fadeFill.changeRectImage(0, (2000-self.strFade)*0.075, "topleft")
		self.fadeFillSurface.blit(self.fadeFill.image, self.fadeFill.rect)
		OPTIONS.getReg("surf_main").blit(self.volumeFillSurface, (494+5+204, 573+5))
		OPTIONS.getReg("surf_main").blit(self.fadeFillSurface, (494+5+204+204, 573+5))
		self.volumeFrame.showStaticImage()
		self.fadeFrame.showStaticImage()
		
		self.instrumentImage.showStaticImage()
		self.notesFrameImage.showStaticImage()
		#self.textSamples.showStaticText()
		#self.textVolume.showStaticText()
		self.textStrFade.showStaticText()
		self.textNotes.showStaticText()
		#self.textCurrentSamples.showText(200, 250)
		#self.textCurrentVolume.showText(200, 450)
		self.textCurrentStrFade.showText(494+78+204+204, 573+96)
		if self.numNotes > 0:
			self.textCurrentNotes.showText(960, 20)
		
		self.frameImage.showStaticImage()
		
		#Проверка на отжатие клавиши и её отрисовка
		for i in range(1, 21):
			if not pygame.mixer.Channel(self.snd[i].channelPlay).get_busy():
				self.isPressedKeyDict[i] = 0
			if self.isPressedKeyDict[i] == 1:
				self.imgPressedKey[i].showStaticImage()
		for i in range(1, 10):
			if self.isPressedKeyDictDrum[i] == 1:
				self.imgPressedKeyDrum[i].showStaticImage()
		
		for i in range(1, 12):
			self.textWhite[i].showStaticText()
		for i in range(12, 21):
			self.textBlack[i].showStaticText()
		
		pygame.display.update()