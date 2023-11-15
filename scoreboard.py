import pygame as pg
from pygame import font
from constants import *

from player import Player

class Scoreboard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.textColor = (TEXT_COLOR)
        self.font = pg.font.SysFont(None, 48)

        self.prepScore()
        self.prepHighScore()
        
    def prepScore(self):
        roundedScore = int(round(self.stats.score, -1))
        scoreStr = "{:,}".format(roundedScore)
        self.scoreImg = self.font.render(scoreStr, True, self.textColor, self.settings.bgColor)

        self.scoreRect = self.scoreImg.get_rect()
        self.scoreRect.centerx = self.screenRect.right - 20
        self.scoreRect.top = 20

    def prepHighScore(self):
        highScore = int(round(self.stats.highScore, -1))
        highScoreStr = "{:,}".format(highScore)

        self.highScoreImg = self.font.render(highScoreStr, True, self.textColor, self.settings.bgColor)
        self.highScoreRect = self.highScoreImg.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top

    def showScore(self):
        self.screen.blit(self.scoreImg, self.scoreRect)
        self.screen.blit(self.highScoreImg, self.highScoreRect)