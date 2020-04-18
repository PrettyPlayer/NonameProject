from game.window.MenuWindow import MenuWindow
from game.window.GameWindow import GameWindow
from game.window.OptionWindow import OptionWindow
from game.system.Registry import Registry, OPTIONS

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