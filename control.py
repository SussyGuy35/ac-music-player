import pygame
import sys
from player import Player

def game_exit():
	pygame.quit()
	sys.exit()

class VolumeController:
	def __init__(self, x: int, y: int, w: int, h: int, border_width: int, music_player: Player) -> None:
		self.music_player = music_player
		self.rect = pygame.Rect(0,0,w,h)
		self.rect.x = x
		self.rect.y = y
		self.border_width = border_width
		self.border_rect = pygame.Rect(self.rect.left - self.border_width, self.rect.top - self.border_width, self.rect.width + self.border_width*2, self.rect.height + self.border_width*2)
		self.is_changing = False

	def draw(self, surf: pygame.Surface) -> None:
		bar_rect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width * (self.music_player.volume/1), self.rect.height)
		pygame.draw.rect(surf, (200,200,200), bar_rect)
		pygame.draw.rect(surf, "white", self.border_rect, self.border_width)
	
	def update(self, draw_surf: pygame.Surface) -> None:
		mouse_pos = pygame.mouse.get_pos()
		is_mouse_button_press = pygame.mouse.get_pressed()[0]

		if not self.is_changing:
			if is_mouse_button_press and self.border_rect.collidepoint(mouse_pos):
				self.is_changing = True
		
		if self.is_changing:
			if not is_mouse_button_press:
				self.is_changing = False

			volume = (mouse_pos[0] - self.rect.left) / self.rect.width
			if volume > 1: volume = 1
			elif volume < 0: volume = 0
			self.music_player.set_volume(volume)
		
		self.draw(draw_surf)

class PlayButton:
	def __init__(self, x: int, y: int, music_player: Player) -> None:
		self.play_image = pygame.image.load("assets/play.png")
		self.pause_image = pygame.image.load("assets/pause.png")
		self.image = self.play_image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.music_player = music_player
	
	def draw(self,surf: pygame.Surface) -> None:
		surf.blit(self.image, self.rect)

	def update(self, draw_surf: pygame.Surface) -> None:
		self.image = self.play_image if not self.music_player.is_playing else self.pause_image
		self.draw(draw_surf)

	def on_click(self) -> None:
		if self.music_player.is_playing: self.music_player.pause()
		else: self.music_player.play()

class QuitButton:
	def __init__(self, x: int, y: int) -> None:
		self.image = pygame.image.load("assets/quit.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def on_click(self) -> None:
		game_exit()

	def update(self, draw_surf: pygame.Surface) -> None:
		self.draw(draw_surf)
	
	def draw(self, surf: pygame.Surface) -> None:
		surf.blit(self.image, self.rect)