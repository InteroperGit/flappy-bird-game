import pygame
import assets
import configs
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.game_start_message import GameStartMessage
from objects.game_over_message import GameOverMessage
from objects.score import Score
from datetime import datetime

class Core():
	def __init__(self):

		pygame.init()

		assets.load_sprites()
		assets.load_audios()

		self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
		self.clock = pygame.time.Clock()
		self.sprites = pygame.sprite.LayeredUpdates()
		self.column_create_event = pygame.USEREVENT

		self.bird, self.game_start_message, self.score = self.__create_game_objects(self.sprites)

		self.running = False
		self.gameover = False
		self.game_started = False
		assets.play_audio("levelend", True)

	def __create_game_objects(self, sprites):
		for i in range(2):
			Background(i, sprites)
			Floor(i, sprites)

		bird = Bird(sprites)
		game_start_message = GameStartMessage(sprites)
		score = Score(sprites)

		return bird, game_start_message, score

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.__stop()

			elif event.type == self.column_create_event and self.game_started:
				Column(self.sprites)

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not self.game_started and not self.gameover:
					self.game_started = True
					self.game_start_message.kill()
					pygame.time.set_timer(self.column_create_event, configs.COLUMN_CREATE_EVENT_PERIOD)
					assets.stop_audio("levelend")
					assets.stop_audio("gameover")
					assets.play_audio("overworld", True)
				if event.key == pygame.K_ESCAPE and self.gameover:
					self.gameover = False
					self.game_started = False
					self.sprites.empty()
					self.bird, self.game_start_message, self.score = self.__create_game_objects(self.sprites)
					assets.play_audio("levelend", True)
				if self.game_started and not self.gameover:
					self.bird.handle_event(event)

	def __draw(self):
		self.screen.fill(0)
		self.sprites.draw(self.screen)
		
		if self.game_started and not self.gameover:
			self.sprites.update()

		pygame.display.update()

	def __check_collisions(self):
		if self.bird.check_collisions(self.sprites) and not self.gameover:
			assets.play_audio("hit")
			self.gameover = True
			self.game_started = False
			GameOverMessage(self.sprites)
			assets.stop_audio("overworld")
			assets.play_audio("gameover")
			pygame.time.set_timer(self.column_create_event, 0)

	def __check_column_pass(self):
		for sprite in self.sprites:
			if type(sprite) is Column and sprite.is_passed():
				self.score.value += 1
				assets.play_audio("point")

	def start(self):
		self.running = True

		while self.running:
			self.__handle_events()
			self.__draw()
			self.__check_collisions()
			self.__check_column_pass()
			self.clock.tick(configs.FPS)

	def __stop(self):
		self.running = False
		assets.stop_audio("overworld")
		pygame.quit()