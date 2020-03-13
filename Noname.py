from game.window import *
from game.registry import *

width = 1920
height = 1080
fullscreen = 0
visiblemouse = True
rungame = True
scene = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.display.set_icon(pygame.image.load(os.path.realpath("img\\papich\\2.png")))
pygame.display.set_caption("Noname")
pygame.mouse.set_visible(visiblemouse)
if fullscreen == 0:
	surf_main = pygame.display.set_mode((width, height))
elif fullscreen == 1:
	surf_main = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

class ManageWindow(object):
	def __init__(self):
		self.gamewindow = GameWindow()
		self.menuwindow = MenuWindow()
	def update(self):
		if scene == 0: #Меню
			self.menuwindow.start(60)
		elif scene == 1: #Игра
			self.gamewindow.start(60)
		elif scene == 2: #Настройки
			self.gamewindow.start(60)

if __name__ == "__main__":
	thegame = ManageWindow()
	while rungame:
		thegame.update()