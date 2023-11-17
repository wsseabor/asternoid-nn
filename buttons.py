import pygame as pg
import pygame.font

class Button:
    def __init__(self, game, message):
        self.screen = game.screen
        self.screenRect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.btnColor = (0, 255, 0)
        self.textColor = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        self.prepMessage(message)

    def prepMessage(self, message):
        self.messageImg = self.font.render(message, True, self.textColor, self.btnColor)
        self.messageImgRect = self.messageImg.get_rect()
        self.messageImgRect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.btnColor, self.rect)
        self.screen.blit(self.messageImg, self.messageImgRect)