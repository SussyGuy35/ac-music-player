import pygame

pygame.init()
pygame.mixer.init()

class Player:
	def __init__(self) -> None:
		self.is_playing = True
		self.audio = None
		self.volume = 1.0
	
	def pause(self) -> None:
		self.is_playing = False
		pygame.mixer.pause()
	
	def stop(self) -> None:
		pygame.mixer.stop()
		self.audio = None
	
	def play(self, audio = None, loop = True):
		self.is_playing = True
		if not audio:
			pygame.mixer.unpause()
		else:
			self.audio = audio
			pygame.mixer.stop()
			if loop:
				self.audio.play(-1)
			else:
				self.audio.play()
		self.audio.set_volume(self.volume)

	def set_volume(self, volume) -> None:
		self.volume = volume
		if self.is_playing: self.audio.set_volume(self.volume)