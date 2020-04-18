from game.visual.Image import Image
from game.system.Registry import Registry, OPTIONS

class Fog(Image):
	def __init__(self):
		self.posX = 0
		self.posY = 0
	def changePos(self, speed):
		self.posX -= speed
		if self.posX < -(OPTIONS.getReg("width")):
			self.posX = 0