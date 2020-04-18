import pygame

class GameEvents():
	def actionEvent(event):
		if event.type == pygame.QUIT:
				self.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if self.numSfx < 2:
					self.numSfx += 1
					self.flagSfx = 1
			if event.key == pygame.K_DOWN:
				if 1 < self.numSfx:
					self.numSfx -= 1
					self.flagSfx = 1
			if event.key == pygame.K_RETURN:
				self.changeFullscreen()
			if event.key == pygame.K_q:
				self.snd1.play()
			if event.key == pygame.K_a:
				self.snd2.play()
			if event.key == pygame.K_w:
				self.snd3.play()
			if event.key == pygame.K_s:
				self.snd4.play()
			if event.key == pygame.K_d:
				self.snd5.play()
			if event.key == pygame.K_r:
				self.snd6.play()
			if event.key == pygame.K_f:
				self.snd7.play()
			if event.key == pygame.K_t:
				self.snd8.play()
			if event.key == pygame.K_g:
				self.snd9.play()
			if event.key == pygame.K_h:
				self.snd10.play()
			if event.key == pygame.K_u:
				self.snd11.play()
			if event.key == pygame.K_j:
				self.snd12.play()
			if event.key == pygame.K_i:
				self.snd13.play()
			if event.key == pygame.K_k:
				self.snd14.play()
			if event.key == pygame.K_o:
				self.snd15.play()
			if event.key == pygame.K_l:
				self.snd16.play()
			if event.key == pygame.K_SEMICOLON:
				self.snd17.play()
			if event.key == pygame.K_LEFTBRACKET:
				self.snd18.play()
			if event.key == pygame.K_QUOTE:
				self.snd19.play()
			if event.key == pygame.K_RIGHTBRACKET:
				self.snd20.play()