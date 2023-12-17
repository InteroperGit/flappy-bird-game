import pygame
import assets
import configs
from objects.background import Background
from objects.floor import Floor
from objects.column import Column

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

clock = pygame.time.Clock()

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()
column_create_event = pygame.USEREVENT

for i in range(2):
	Background(i, sprites)
	Floor(i, sprites)

Column(sprites)

pygame.time.set_timer(column_create_event, configs.COLUMN_CREATE_EVENT_PERIOD)

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == column_create_event:
			Column(sprites)

	screen.fill("pink")

	sprites.draw(screen)
	sprites.update()

	pygame.display.flip()
	clock.tick(configs.FPS)

pygame.quit()