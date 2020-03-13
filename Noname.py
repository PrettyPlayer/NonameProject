from game.window import *

width = 1920
height = 1080

class InitGame():
	def __init__(self):
		self.fullscreen = 0
		self.visiblemouse = True
		self.rungame = True
		
		self.centeredwindow()
		self.preinitsound()
		self.initwindow()
		self.setvisisblemouse()
	def centeredwindow(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
	def preinitsound(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
	def initwindow(self):
		pygame.init()
		pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\papich\\2.png")))
		self.fullscreenchange()
		pygame.display.set_caption("Noname")
	def setvisisblemouse(self):
		pygame.mouse.set_visible(self.visiblemouse)
	def initstart(self, copy):
		self.managegame = ManageGame(copy)
		while self.rungame:
			self.managegame.update()
	def fullscreenchange(self):
		if self.fullscreen == 0:
			self.surf_main = pygame.display.set_mode((width, height))
		elif self.fullscreen == 1:
			self.surf_main = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

class ManageGame():
	def __init__(self, copy):
		self.scene = 0
		self.gamewindow = GameWindow(copy)
		self.menuwindow = MenuWindow(copy)
	def update(self):
		if self.scene == 0:
			self.menuwindow.start(60)
		elif self.scene == 1:
			self.gamewindow.start(60)

if __name__ == "__main__":
	thegame = InitGame()
	thegame.initstart(thegame)