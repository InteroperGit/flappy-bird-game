import pygame.sprite
import configs
import assets

class Background(pygame.sprite.Sprite):
	def __init__(self, index, *groups):

		self.image = assets.get_sprite("background")
		self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))

		super().__init__(*groups)

	def update(self):
		self.rect.x -= configs.MOVE_SPEED

		if self.rect.right <= 0:
			self.rect.x = configs.SCREEN_WIDTH