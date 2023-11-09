import pygame as pg
from constants import *


class Player(pg.sprite.Sprite):
    def __init__(self, settings, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pg.image.load(playerTexture)
        self.rect = self.image.get_rect()
        self.screenRect = self.get_rect()

        self.rect.midbottom = self.screenRect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def center(self):
        self.rect.midbottom = self.screenRect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        if self.moveRight and self.rect.right < self.screenRect.right:
            self.x += self.settings.speed
        if self.moveLeft and self.rect.left > self.screenRect.left:
            self.x -= self.settings.speed
        if self.moveUp and self.rect.top > 0:
            self.y -= self.settings.shipSpeed
        if self.moveDown and self.rect.bottom < self.screenRect.bottom:
            self.y += self.settings.shipSpeed
        
        self.rect.x = self.x
        self.rect.y = self.y