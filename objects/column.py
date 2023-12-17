import pygame
import pygame.sprite
import pygame.transform
import configs
import assets
import random

class Column(pygame.sprite.Sprite):
	def __init__(self, *groups):

		self.gap = configs.PIPE_GAP
		self.sprite = assets.get_sprite("pipe-green")
		self.sprite_rect = self.sprite.get_rect()

		self.bottom_pipe = self.sprite
		self.bottom_pipe_rect = self.bottom_pipe.get_rect(
			topleft=(0, self.sprite_rect.height + self.gap)
		)

		self.top_pipe = pygame.transform.flip(self.sprite, flip_x=False, flip_y=True)
		self.top_pipe_rect = self.top_pipe.get_rect(topleft=(0, 0))

		self.image = pygame.surface.Surface(
			(
				self.sprite_rect.width,
			 	self.sprite_rect.height * 2 + self.gap
			),
			pygame.SRCALPHA
		)
		self.image.blit(self.bottom_pipe, self.bottom_pipe_rect)
		self.image.blit(self.top_pipe, self.top_pipe_rect)

		sprite_floor_height = assets.get_sprite("floor").get_rect().height
		min_y = configs.PIPE_MIN_Y
		max_y = configs.SCREEN_HEIGHT - sprite_floor_height - configs.PIPE_MIN_Y

		self.rect = self.image.get_rect(
			midleft=(
				configs.SCREEN_WIDTH, 
				random.uniform(min_y, max_y)
			)
		)

		super().__init__(*groups)

	
	def update(self):
		self.rect.x -= configs.PIPE_MOVE_SPEED

