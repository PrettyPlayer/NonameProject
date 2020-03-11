import os, sys
import pygame
from random import randint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Noname import *

class Window():
	def __init__(self, copy):
		self.run = True
		global thegame
		thegame = copy
	def start(self, Frames):
		global FPS
		FPS = Frames
		self.clock = pygame.time.Clock()
		self.preinit()
		while self.run:
			self.postinit()
			self.exit()
			pygame.display.update()
			self.clock.tick(FPS)
	def exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
				sys.exit()

class MenuWindow(Window):
	def preinit(self):
		self.backgroundmusic = Music("sfx\\music.wav")
		self.backgroundmusic.start(300, -1)
		
		self.backgroundmenuimage = Image()
		self.backgroundmenupapichimage = Image()
		self.backgroundmenublackimage = Image()
		
		self.snowanimation = Animation(29)
		
		self.backgroundmenuimage.createcenterimage("img\\backgroundmenu\\", "backgroundmenuimage", 960, 540)
		self.backgroundmenupapichimage.createbottomleftimage("img\\backgroundmenu\\", "backgroundmenupapich", 160, 1080)
		self.backgroundmenublackimage.createcenterimage("img\\backgroundmenu\\", "backgroundmenublack", 960, 540)
	def postinit(self):
		self.snowanimation.update("img\\snow\\", 2)
		self.backgroundmenuimage.show()
		self.snowanimation.show()
		self.backgroundmenupapichimage.show()
		self.backgroundmenublackimage.show()

class GameWindow(Window):
	def preinit(self):
		pass
	def postinit(self):
		pass

class Image(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	def loadsprite(self, path, name):
		self.image = pygame.image.load(os.path.realpath(path + str(name) + ".png")).convert_alpha()
	def scale(self, sizex=1, sizey=1):
		self.image = pygame.transform.scale(self.image, (self.image.get_width()*self.changesizex(sizex), self.image.get_height()*self.changesizey(sizey)))
	def createcenterrect(self, posx, posy):
		self.rect = self.image.get_rect(center=(self.changex(posx), self.changey(posy)))
	def createbottomleftrect(self, posx, posy):
		self.rect = self.image.get_rect(bottomleft=(self.changex(posx), self.changey(posy)))
	def createcenterimage(self, path, name, posx, posy, sizex=1, sizey=1):
		self.loadsprite(path, name)
		self.scale(sizex, sizey)
		self.createcenterrect(posx, posy)
	def createbottomleftimage(self, path, name, posx, posy, sizex=1, sizey=1):
		self.loadsprite(path, name)
		self.scale(sizex, sizey)
		self.createbottomleftrect(posx, posy)
	def show(self):
		thegame.surf_main.blit(self.image, self.rect)
	def changex(self, x):
		return(round(x/1920*width))
	def changey(self, y):
		return(round(y/1080*height))
	def changesizex(self, sizex):
		return(round(sizex*width/1920))
	def changesizey(self, sizey):
		return(round(sizey*height/1080))

class Animation(Image):
	def __init__(self, num):
		self.currenttime=0
		self.currentnum=1
		self.maxnum=num
	def updatenum(self):
		if 0<self.currentnum<self.maxnum:
			self.currentnum+=1
		elif self.currentnum == self.maxnum:
			self.currentnum = 1
		else:
			print("Error updatenum()")
	def updatetime(self):
		self.currenttime+=1
	def update(self, path, speed):
		if self.currenttime%self.changespeed(speed) == 0:
			self.createcenterimage(path, self.currentnum, 960, 540)
			self.updatenum()
		self.updatetime()
	def changespeed(self, speed):
		return(round(speed*FPS/60))

class Music():
	def __init__(self, path):
		self.music = pygame.mixer.music.load(path)
	def pauseupload(self, time):
		self.music = pygame.time.wait(time)
	def play(self, times):
		self.music = pygame.mixer.music.play(times)
	def start(self, time=300, times=-1):
		self.pauseupload(time)
		self.play(times)