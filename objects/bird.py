import pygame
import pygame.sprite
import pygame.mask
import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor

class Bird(pygame.sprite.Sprite):
	def __init__(self, *groups):
		self._layer = Layer.PLAYER

		self.images = [
			assets.get_sprite("redbird-upflap"), #0
			assets.get_sprite("redbird-midflap"), #1
			assets.get_sprite("redbird-downflap"), #2
			assets.get_sprite("redbird-midflap"), #3
		]

		self.image_index = 0
		self.image = self.images[self.image_index]
		self.rect = self.image.get_rect(topleft=
			(
				-configs.BIRD_START_Y_POS, 
				configs.BIRD_START_X_POS
			))

		self.mask = pygame.mask.from_surface(self.image)

		self.flap = 0

		self.collision_num = 0

		super().__init__(*groups)

	def update(self):
		self.image_index = (self.image_index + 1) % len(self.images)
		self.image = self.images[self.image_index]
		self.mask = pygame.mask.from_surface(self.image)

		self.flap += configs.GRAVITY
		self.rect.y += self.flap

		if self.rect.x < configs.BIRD_START_X_POS:
			self.rect.x += configs.BIRD_X_POS_INCREMENT

	def handle_event(self, event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			self.flap = 0
			self.flap -= configs.BIRD_FLY_UP_COEFF

	def check_collisions(self, sprites):
		is_above_ceil = self.rect.bottom < 0

		if is_above_ceil:
			return True

		for sprite in sprites:
			is_column = type(sprite) is Column
			is_floor = type(sprite) is Floor
			is_damage = (is_column or is_floor) and sprite.mask.overlap(self.mask, 
					(self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y))
			
			if is_damage:
				return True

		return False

