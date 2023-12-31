import pygame as pg
from constants import *

class Asteroid(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pg.image.load(asteroidTexture)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y -= (self.settings.astSpeed)
        self.rect.y = self.y