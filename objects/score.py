import pygame.sprite
from layer import Layer
import assets
import configs
from pygame.surface import Surface

class Score(pygame.sprite.Sprite):
	def __init__(self, *groups):
		self._layer = Layer.UI
		self.value = 0
		self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT / 2))
		self.images = []
		self.height = 0
		self.width = 0
		self.str_value = ""
		self.image = None
		self.rect = None
	
		self.__create()
		super().__init__(*groups)

	def __create(self):
		self.str_value = str(self.value)
		self.images = []
		self.width = 0

		for str_value_char in self.str_value:
			img = assets.get_sprite(str_value_char)
			self.images.append(img)
			self.width += img.get_width()
			self.height = img.get_height()

		self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
		self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, configs.SCORE_Y_POS))

		x = 0
		for img in self.images:
			self.image.blit(img, (x, 0))
			x += self.width

	def update(self):
		self.__create()


