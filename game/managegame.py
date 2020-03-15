from game.menuwindow import MenuWindow
from game.gamewindow import GameWindow
from game.optionwindow import OptionWindow
from game.registry import Registry, OPTIONS

class ManageGame(object):
	
	def __init__(self):
		self.gamewindow = GameWindow()
		self.menuwindow = MenuWindow()
		self.optionwindow = OptionWindow()
	
	def update(self):
		if OPTIONS.getReg("scene") == 0:
			self.menuwindow.start(60)
		elif OPTIONS.getReg("scene") == 1:
			self.gamewindow.start(60)
		elif OPTIONS.getReg("scene") == 2:
			self.optionwindow.start(60)