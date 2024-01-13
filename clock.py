import pygame
import datetime

class Clock:
	def __init__(self, x: int, y: int, font: pygame.Font) -> None:
		self.color = (255,255,255)
		self.aa_enabled = True
		self.image = font.render("00:00:00",self.aa_enabled,self.color)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.centerx = self.x
		self.rect.centery = self.y
		self.font = font

	def draw(self, surf: pygame.Surface) -> None:
		surf.blit(self.image, self.rect)

	def update(self, draw_surf: pygame.Surface) -> None:
		self.image = self.font.render(datetime.datetime.now().strftime("%X"), self.aa_enabled, self.color)
		self.rect = self.image.get_rect()
		self.rect.centerx = self.x
		self.rect.centery = self.y
		self.draw(draw_surf)
