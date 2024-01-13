import pygame 
import sys, random, datetime
import player
from clock import Clock
import control
from control import PlayButton, VolumeController, QuitButton

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GAMESPEED = 30
TITLE = "Animal Crossing Music Player"
ICON = pygame.image.load("assets/icon.jpg")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.NOFRAME)
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

play_button = PlayButton(5, SCREEN_HEIGHT-70-5, music_player)
volume_control_bar = VolumeController(SCREEN_WIDTH-300-10, SCREEN_HEIGHT-50-10, 300, 50, 3, music_player)
display_clock = Clock(SCREEN_WIDTH/2, SCREEN_HEIGHT/3, font)
quit_button = QuitButton(5,5)

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			control.game_exit
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if play_button.rect.collidepoint(event.pos):
				play_button.on_click()
			
			elif quit_button.rect.collidepoint(event.pos):
				quit_button.on_click()
	
	update_hour_music()

	screen.fill("black")
	play_button.update(draw_surf=screen)
	volume_control_bar.update(draw_surf=screen)
	display_clock.update(draw_surf=screen)
	quit_button.update(draw_surf=screen)

	pygame.display.flip()
	clock.tick(GAMESPEED)