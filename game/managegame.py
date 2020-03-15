from game.MenuWindow import MenuWindow
from game.GameWindow import GameWindow
from game.OptionWindow import OptionWindow
from game.Registry import Registry, OPTIONS

class ManageGame(object):
	
	def __init__(self):
		self.gameWindow = GameWindow()
		self.menuWindow = MenuWindow()
		self.optionWindow = OptionWindow()
	
	def update(self):
		if OPTIONS.getReg("scene") == 0:
			self.menuWindow.start(60)
		elif OPTIONS.getReg("scene") == 1:
			self.gameWindow.start(60)
		elif OPTIONS.getReg("scene") == 2:
			self.optionWindow.start(60)