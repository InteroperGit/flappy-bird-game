import pygame
import assets
import configs
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird

def create_game_objects(sprites):
	for i in range(2):
		Background(i, sprites)
		Floor(i, sprites)

	Column(sprites)
	bird = Bird(sprites)

	return [bird]

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

clock = pygame.time.Clock()

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()
column_create_event = pygame.USEREVENT

[bird] = create_game_objects(sprites)

pygame.time.set_timer(column_create_event, configs.COLUMN_CREATE_EVENT_PERIOD)

running = True
gameover = False
score = 0

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == column_create_event:
			Column(sprites)

		bird.handle_event(event)

	screen.fill(0)

	sprites.draw(screen)
	
	if not gameover:
		sprites.update()

	if bird.check_collisions(sprites):
		gameover = True

	for sprite in sprites:
		if type(sprite) is Column and sprite.is_passed():
			score += 1

	print(f'score = [{score}]')

	pygame.display.flip()
	clock.tick(configs.FPS)

pygame.quit()