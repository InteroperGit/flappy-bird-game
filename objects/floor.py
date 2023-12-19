import pygame.sprite
import pygame.mask
import configs
import assets
from layer import Layer

class Floor(pygame.sprite.Sprite):
	def __init__(self, index, *groups):

		self._layer = Layer.FLOOR
		self.image = assets.get_sprite("floor")
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 
				configs.SCREEN_HEIGHT - self.image.get_height()))
		super().__init__(*groups)

	def update(self):
		self.rect.x -= configs.MOVE_SPEED

		if self.rect.right <= 0:
			self.rect.x = configs.SCREEN_WIDTH