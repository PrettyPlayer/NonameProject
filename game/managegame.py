from game.menuwindow import MenuWindow
from game.gamewindow import GameWindow
from game.registry import Reg

class ManageGame(object):
	
	def __init__(self):
		self.scene = 0
		self.gamewindow = GameWindow()
		self.menuwindow = MenuWindow()
	
	def update(self):
		if self.scene == 0:
			self.menuwindow.start(60)
		elif self.scene == 1:
			self.gamewindow.start(60)