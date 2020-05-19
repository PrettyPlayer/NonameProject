import os
import pygame

#Параметры
FPS = 1
WIDTH = 200
HEIGHT = 400
fullscreen = 1

CYAN = (0, 255, 255)

#Вёрстка окна
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
surf_main = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer")
clock = pygame.time.Clock()

def start(time):
	if run==True:
		time[3][1]+=1/FPS
		if time[3][1]>=60:
			time[2][1]+=1
			time[3][1]=time[3][1]-60
		if time[2][1]==60:
			time[1][1]+=1
			time[2][1]=0
		if time[1][1]==24:
			time[0][1]+=1
			time[1][1]=0
		#Смена секунд
		if time[3][1]%10==0 or 5<=time[3][1]%10<=9 or 11<=time[3][1]<=14:
			time[3][0]="Секунд"
		elif time[3][1]%10==1:
			time[3][0]="Секунда"
		elif 2<=time[3][1]%10<=4:
			time[3][0]="Секунды"
		#Смена минут
		if time[2][1]%10==0 or 5<=time[2][1]%10<=9 or 11<=time[2][1]<=14:
			time[2][0]="Минут"
		elif time[2][1]%10==1:
			time[2][0]="Минута"
		elif 2<=time[2][1]%10<=4:
			time[2][0]="Минуты"
		#Смена часов
		if time[1][1]%10==0 or 5<=time[1][1]<=20:
			time[1][0]="Часов"
		elif time[1][1]%10==1:
			time[1][0]="Час"
		elif 2<=time[1][1]%10<=4:
			time[1][0]="Часа"
		#Смена дней
		if time[0][1]%10==0 or 5<=time[0][1]<=20:
			time[0][0]="Дней"
		elif time[0][1]%10==1:
			time[0][0]="День"
		elif 2<=time[0][1]%10<=4:
			time[0][0]="Дня"
def save(time):
	f = open("time.txt", "w", encoding="utf-8")
	f.write(time[0][0] + "\t" + str(time[0][1]) + "\n" + time[1][0] + "\t" + str(time[1][1]) + "\n" + time[2][0] + "\t" + str(time[2][1]) + "\n" + time[3][0] + "\t" + str(round(time[3][1])))
	f.close()
	f = open("..\\README.md", "w", encoding="utf-8")
	f.write("<h1><center>Рабочий файл - Noname.py</center></h1><h3><center>Потраченное время на проект:</center><center><pre>" + time[0][0] + "\t" + str(time[0][1]) + "\n" + time[1][0] + "\t" + str(time[1][1]) + "\n" + time[2][0] + "\t" + str(time[2][1]) + "\n" + time[3][0] + "\t" + str(round(time[3][1])) + "</pre></center></h3><h4>Про таймер я совсем забыл, часы не считал уже давно .-.</h4><h2>Управление:</h2><h3>Стрелочки влево/вправо для навигации среди опций, пока их 2</h3><h3>Стрелочки вверх/вниз меняют выбранную опцию</h3>")
	#f.write("<h1><center>Рабочий файл - Noname.py</center></h1><h3><center>Потраченное время на проект:</center><center><pre>" + time[0][0] + "\t" + str(time[0][1]) + "\n" + time[1][0] + "\t" + str(time[1][1]) + "\n" + time[2][0] + "\t" + str(time[2][1]) + "\n" + time[3][0] + "\t" + str(round(time[3][1])) + "</pre></center></h3>" + """<h5><a href="https://youtu.be/UryFjJnok6I">Кликабельный скриншот (видео)</a></h5><a style="float:right" href="https://youtu.be/UryFjJnok6I" target="_blank">  <img alt="Papich Gameplay" src="https://img.youtube.com/vi/UryFjJnok6I/maxresdefault.jpg" /></a>""")
	f.close()

class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, size, filename, text, font, sizetext, color):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.image = pygame.image.load(os.path.realpath("Sprites\\button\\" + filename + ".png"))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*size), int(self.image.get_height()*size)))
		self.rect = self.image.get_rect(center=(x, y))
		self.sx=self.image.get_width()
		self.sy=self.image.get_height()
		self.font = pygame.font.Font("Fonts\\" + font, sizetext)
		self.text = self.font.render(text, 1, color)
		self.place = self.text.get_rect(center=(self.sx//2, self.sy//2))
		self.name = text
	def click(self, pos):
		if self.x-(self.sx//2) <= pos[0] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= pos[1] <= self.y+(self.sy//2):
			if self.name == "Играть":
				GameWindow()

class Text(pygame.sprite.Sprite):
	def __init__(self, font, sizetext):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.SysFont(font, sizetext, bold=False, italic=False)
	def show(self, text, x, y, color):
		self.text = self.font.render(str(text), 1, color)
		self.place = self.text.get_rect(topleft=(x, y))

try:
	f = open("time.txt", "r", encoding="utf-8")
	time = f.read().split("\n")
	f.close()
	for i in range(0, len(time)):
		time[i]=time[i].split("\t")
		time[i][1] = round(float(time[i][1]))
except:
	try:
		f = open("time.txt", "x")
	except:
		pass
	f = open("time.txt", "w", encoding="utf-8")
	f.write("Дней\t00\nЧасов\t00\nМинут\t00\nСекунд\t00")
	f = open("time.txt", "r", encoding="utf-8")
	time = f.read().split("\n")
	f.close()
	for i in range(0, len(time)):
		time[i]=time[i].split("\t")
		time[i][1] = int(time[i][1])
text0 = Text("arial", 24)
text1 = Text("arial", 24)
text2 = Text("arial", 24)
text3 = Text("arial", 24)
text4 = Text("arial", 24)
text5 = Text("arial", 24)
text6 = Text("arial", 24)
text7 = Text("arial", 24)
text8 = Text("arial", 24)
backwindow = pygame.image.load(os.path.realpath("img//back.png"))
backwindow_rect = backwindow.get_rect(center=(int(WIDTH/2), int(HEIGHT/2)))
play = pygame.image.load(os.path.realpath("img//play.png"))
play = pygame.transform.scale(play, (100, 100))
play_rect = play.get_rect(center=(50, 300))
pause = pygame.image.load(os.path.realpath("img//pause.png"))
pause = pygame.transform.scale(pause, (100, 100))
pause_rect = pause.get_rect(center=(150, 300))
sfx1=pygame.mixer.Sound("sfx//1.wav")
sfx2=pygame.mixer.Sound("sfx//2.wav")
run=False
while True:
	text0.show("Проебано времени:", 10, 10, CYAN)
	text1.show(time[0][0], 40, 50, CYAN)
	text2.show(time[0][1], 130, 50, CYAN)
	text3.show(time[1][0], 40, 80, CYAN)
	text4.show(time[1][1], 130, 80, CYAN)
	text5.show(time[2][0], 40, 110, CYAN)
	text6.show(time[2][1], 130, 110, CYAN)
	text7.show(time[3][0], 40, 140, CYAN)
	text8.show(int(time[3][1]), 130, 140, CYAN)
	surf_main.blit(backwindow, backwindow_rect)
	surf_main.blit(play, play_rect)
	surf_main.blit(pause, pause_rect)
	surf_main.blit(text0.text, text0.place)
	surf_main.blit(text1.text, text1.place)
	surf_main.blit(text2.text, text2.place)
	surf_main.blit(text3.text, text3.place)
	surf_main.blit(text4.text, text4.place)
	surf_main.blit(text5.text, text5.place)
	surf_main.blit(text6.text, text6.place)
	surf_main.blit(text7.text, text7.place)
	surf_main.blit(text8.text, text8.place)
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save(time)
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if 0<event.pos[0]<100 and 250<event.pos[1]<350:
					channel2=sfx2.stop()
					channel1=sfx1.stop()
					run=True
					channel2=sfx2.play()
				elif 100<event.pos[0]<200 and 250<event.pos[1]<350:
					channel2=sfx2.stop()
					channel1=sfx1.stop()
					run=False
					channel1=sfx1.play()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					save(time)
					sys.exit()
	start(time)
	pygame.display.update()
	clock.tick(FPS)