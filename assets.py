import os
import pygame
import pygame.mixer

sprites = {}
audios = {}

def load_sprites():
	path = os.path.join("assets", "sprites")

	for file in os.listdir(path):
		sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
	return sprites[name]

def load_audios():
	path = os.path.join("assets", "audios")

	for file in os.listdir(path):
		audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name, loops=False):
	audios[name].play(loops=loops)

def stop_audio(name):
	audios[name].stop()