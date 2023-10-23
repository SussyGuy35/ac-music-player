import pygame, sys, datetime, random
import player

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GAMESPEED = 30
TITLE = "Animal Crossing Music Player"
ICON = pygame.image.load("assets/icon.jpg")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)

clock = pygame.time.Clock()

font = pygame.font.Font("assets/font.ttf", 69)

music_player = player.Player()

game = "wild-world"
weathers = ["sunny", "rainy", "snowy"]
time = 0

def play_hour_music():
	weather = random.choice(weathers)
	music_player.play(pygame.mixer.Sound(f"music/{game}/{time}_{weather}.ogg"))

def update_hour_music():
	global time
	if music_player.is_playing:
		new_time = datetime.datetime.now().hour
		if new_time != time:
			time = new_time
			play_hour_music()

class PlayButton:
	def __init__(self) -> None:
		self.play_image = pygame.image.load("assets/play.png")
		self.pause_image = pygame.image.load("assets/pause.png")
		self.image = self.play_image
		self.rect = self.image.get_rect()
		self.rect.bottom = SCREEN_HEIGHT - 5
		self.rect.left = 5
	
	def draw(self,surf: pygame.Surface) -> None:
		surf.blit(self.image, self.rect)

	def update(self) -> None:
		self.image = self.play_image if not music_player.is_playing else self.pause_image
		self.draw(screen)

	def on_click(self) -> None:
		if music_player.is_playing: music_player.pause()
		else: music_player.play()

class VolumeController:
	def __init__(self) -> None:
		self.rect = pygame.Rect(0,0,300,50)
		self.rect.bottom = SCREEN_HEIGHT - 10
		self.rect.right = SCREEN_WIDTH - 10
		self.border_width = 3
		self.border_rect = pygame.Rect(self.rect.left - self.border_width, self.rect.top - self.border_width, self.rect.width + self.border_width*2, self.rect.height + self.border_width*2)

	def draw(self, surf: pygame.Surface) -> None:
		bar_rect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width * (music_player.volume/1), self.rect.height)
		pygame.draw.rect(surf, (200,200,200), bar_rect)
		pygame.draw.rect(surf, "white", self.border_rect, self.border_width)
	
	def update(self) -> None:
		if pygame.mouse.get_pressed()[0]:
			mouse_pos = pygame.mouse.get_pos()
			if self.border_rect.collidepoint(mouse_pos):
				volume = (mouse_pos[0] - self.rect.left) / self.rect.width
				if volume > 1: volume = 1
				elif volume < 0: volume = 0
				music_player.set_volume(volume)
		self.draw(screen)

class Clock:
	def __init__(self) -> None:
		self.color = (255,255,255)
		self.aa_enabled = True
		self.image = font.render("00:00:00",self.aa_enabled,self.color)
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH/2
		self.rect.centery = SCREEN_HEIGHT/3

	def draw(self, surf: pygame.Surface) -> None:
		surf.blit(self.image, self.rect)

	def update(self) -> None:
		self.image = font.render(datetime.datetime.now().strftime("%X"), self.aa_enabled, self.color)
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH/2
		self.rect.centery = SCREEN_HEIGHT/3
		self.draw(screen)

play_button = PlayButton()
volume_control_bar = VolumeController()
display_clock = Clock()

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if play_button.rect.collidepoint(event.pos):
				play_button.on_click()
	
	update_hour_music()

	screen.fill("black")
	play_button.update()
	volume_control_bar.update()
	display_clock.update()

	pygame.display.flip()
	clock.tick(GAMESPEED)