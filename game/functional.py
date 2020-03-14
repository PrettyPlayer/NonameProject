class Image(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	def loadimage(self, path, name):
		self.image = pygame.image.load(os.path.realpath(path + str(name) + ".png")).convert_alpha()
	def scale(self, sizex=1, sizey=1):
		self.image = pygame.transform.scale(self.image, (round(self.image.get_width()*self.changesizex(sizex)), round(self.image.get_height()*self.changesizey(sizey))))
	def createrectimage(self, posx, posy, pos="center"):
		if pos == "center":
			self.rect = self.image.get_rect(center=(self.changex(posx), self.changey(posy)))
		elif pos == "top":
			self.rect = self.image.get_rect(top=(self.changex(posx), self.changey(posy)))
		elif pos == "topleft":
			self.rect = self.image.get_rect(topleft=(self.changex(posx), self.changey(posy)))
		elif pos == "topright":
			self.rect = self.image.get_rect(topright=(self.changex(posx), self.changey(posy)))
		elif pos == "left":
			self.rect = self.image.get_rect(left=(self.changex(posx), self.changey(posy)))
		elif pos == "right":
			self.rect = self.image.get_rect(right=(self.changex(posx), self.changey(posy)))
		elif pos == "bottom":
			self.rect = self.image.get_rect(bottom=(self.changex(posx), self.changey(posy)))
		elif pos == "bottomleft":
			self.rect = self.image.get_rect(bottomleft=(self.changex(posx), self.changey(posy)))
		elif pos == "bottomright":
			self.rect = self.image.get_rect(bottomright=(self.changex(posx), self.changey(posy)))
	def createimage(self, path, name, sizex=1, sizey=1):
		self.loadimage(path, name)
		self.scale(sizex, sizey)
	def showimage(self, posx, posy, pos="center"):
		self.pos=pos
		self.createrectimage(posx, posy, self.pos)
		surf_main.blit(self.image, self.rect)
	def changex(self, x):
		return(round(x/1920*width))
	def changey(self, y):
		return(round(y/1080*height))
	def changesizex(self, sizex):
		if width>1920:
			return(sizex*width/1920)
		else:
			return(sizex)
	def changesizey(self, sizey):
		if height>1080:
			return(sizey*height/1080)
		else:
			return(sizey)

class Text(Image):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	def loadtext(self, text, font, sizetext, color):
		self.text = pygame.font.Font("fonts\\" + font + ".ttf", sizetext)
		self.text = self.text.render(text, 1, color)
	def createrecttext(self, posx, posy):
		self.textrect = self.text.get_rect(center=(self.changex(posx), self.changey(posy)))
	def showtext(self, posx, posy):
		self.createrecttext(posx, posy)
		surf_main.blit(self.text, self.textrect)

class Button(Text):
	def __init__(self, name):
		self.name = name
		pygame.sprite.Sprite.__init__(self)
	def loadbutton(self, name, text, font, sizetext, color, sizex=1, sizey=1):
		self.sizex = sizex
		self.sizey = sizey
		self.createimage("img\\button\\", name, self.sizex, self.sizey)
		self.loadtext(text, font, sizetext, color)
	def showbutton(self, posx, posy, pos="center"):
		self.posx = posx
		self.posy = posy
		self.pos = pos
		self.showimage(posx, posy, self.pos)
		self.showtext(posx, posy)
	def click(self, mousepos):
		if self.rect[0] <= mousepos[0] <= self.rect[0]+self.rect[2] and self.rect[1] <= mousepos[1] <= self.rect[1]+self.rect[3]:
			if self.name == "start":
				menuwindow.backgroundmusic.stop()
				scene = 1
				menuwindow.run = False
			elif self.name == "settings":
				pass
			elif self.name == "exit":
				quit()
				sys.exit()

class Animation(Image):
	def __init__(self, path, num):
		self.currenttime=0
		self.currentnum=1
		self.maxnum=num
		self.image={}
		self.path=path
	def get(self, posx, posy, sizex=1, sizey=1):
		self.posx = posx
		self.posy = posy
		self.sizex = sizex
		self.sizey = sizey
	def genlist(self):
		self.image={x: Image() for x in range(1, self.maxnum+1)}
	def loadallimage(self, sizex=1, sizey=1):
		self.genlist()
		for i in range(1, self.maxnum+1):
			self.image[i].createimage(self.path, i, sizex, sizey)
	def updatenum(self):
		if 0<self.currentnum<self.maxnum:
			self.currentnum+=1
		elif self.currentnum == self.maxnum:
			self.currentnum = 1
		else:
			print("Error updatenum()")
	def updatetime(self):
		self.currenttime+=1
	def showanimation(self, posx, posy, speed):
		if self.currenttime%self.changespeed(speed) == 0:
			self.image[self.currentnum].showimage(posx, posy)
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
	def stop(self):
		self.music = pygame.mixer.music.stop()