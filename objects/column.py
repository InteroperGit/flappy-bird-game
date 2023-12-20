import pygame
import pygame.sprite
import pygame.mask
import pygame.transform
import configs
import assets
import random
from layer import Layer

class Column(pygame.sprite.Sprite):
	def __create_image(self):
		image = pygame.surface.Surface(
			(
				self.sprite_rect.width,
			 	self.sprite_rect.height * 2 + self.gap
			),
			pygame.SRCALPHA
		)

		image.blit(self.bottom_pipe, self.bottom_pipe_rect)
		image.blit(self.top_pipe, self.top_pipe_rect)

		return image

	def __init__(self, *groups):

		self._layer = Layer.OBSTACLE
		self.gap = configs.PIPE_GAP
		self.sprite = assets.get_sprite("pipe-green")
		self.sprite_rect = self.sprite.get_rect()

		self.bottom_pipe = self.sprite
		self.bottom_pipe_rect = self.bottom_pipe.get_rect(
			topleft=(0, self.sprite_rect.height + self.gap)
		)

		self.top_pipe = pygame.transform.flip(self.sprite, flip_x=False, flip_y=True)
		self.top_pipe_rect = self.top_pipe.get_rect(topleft=(0, 0))

		self.image = self.__create_image()

		self.mask = pygame.mask.from_surface(self.image)

		sprite_floor_height = assets.get_sprite("floor").get_rect().height
		min_y = configs.PIPE_MIN_Y
		max_y = configs.SCREEN_HEIGHT - sprite_floor_height - configs.PIPE_MIN_Y

		self.rect = self.image.get_rect(
			midleft=(
				configs.SCREEN_WIDTH * 2, 
				random.uniform(min_y, max_y)
			)
		)

		self.passed = False

		super().__init__(*groups)

	
	def update(self):
		self.rect.x -= configs.PIPE_MOVE_SPEED

		if self.rect.right <= 0:
			self.kill()

	def is_passed(self):
		if self.rect.x < configs.COLUMN_IS_PASSED_X and not self.passed:
			self.passed = True
			return True

		return False

