class Registry():
	
	def __init__(self):
		self.reg = {"scene": 1, "visibleMouse": True, "fullScreen": 0, "width": 1920, "height": 1080}
	
	def setReg(self, key, value):
		self.reg[key] = value
	
	def getReg(self, key):
		if key in self.reg:
			return self.reg[key]

OPTIONS = Registry()