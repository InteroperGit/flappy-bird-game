import pygame
import assets
import configs
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.game_start_message import GameStartMessage
from objects.game_over_message import GameOverMessage
from datetime import datetime

def create_game_objects(sprites):
	for i in range(2):
		Background(i, sprites)
		Floor(i, sprites)

	bird = Bird(sprites)

	game_start_message = GameStartMessage(sprites)

	return bird, game_start_message

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

clock = pygame.time.Clock()

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()
column_create_event = pygame.USEREVENT

bird, game_start_message = create_game_objects(sprites)

running = True
gameover = False
score = 0
game_started = False

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == column_create_event and game_started:
			Column(sprites)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and not game_started and not gameover:
				game_started = True
				game_start_message.kill()
				pygame.time.set_timer(column_create_event, configs.COLUMN_CREATE_EVENT_PERIOD)
			if event.key == pygame.K_ESCAPE and gameover:
				gameover = False
				game_started = False
				sprites.empty()
				bird, game_start_message = create_game_objects(sprites)

		bird.handle_event(event)

	screen.fill(0)

	sprites.draw(screen)
	
	if game_started and not gameover:
		sprites.update()

	if bird.check_collisions(sprites):
		gameover = True
		game_started = False
		GameOverMessage(sprites)
		pygame.time.set_timer(column_create_event, 0)

	for sprite in sprites:
		if type(sprite) is Column and sprite.is_passed():
			score += 1

	pygame.display.flip()
	clock.tick(configs.FPS)

pygame.quit()