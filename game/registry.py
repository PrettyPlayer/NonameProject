class Reg():
	
	reg = {"fullscreen": 0, "visiblemouse": True, "rungame": True, "width": 1920, "height": 1080}
	def setreg(key, value):
		reg[key] = value
	
	def getreg(key):
		if key in reg:
			return reg[key]