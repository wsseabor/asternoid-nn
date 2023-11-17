#/usr/bin/env/python3

import pygame as pg
from pygame.sprite import Group
import os
import sys
from constants import *
from stats import Stats
from player import Player
from asteroid import Asteroid
from settings import Settings
from buttons import Button

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screenWidth, self.settings.screenHeight)
        )
        pg.display.set_caption(WIN_TITLE)

        self.stats = Stats(self)

        self.gameActive = False

        self.player = Player(self)
        self.asteroids = pg.sprite.Group()

        self.playBtn = Button(self, PLAY_TITLE)

    def run(self):
        while True:
            self._checkAllEvents()

            if self.gameActive:
                self.player.update()
                
            self._update()
            self.clock.tick(FPS)

    def _checkPlay(self, mousePos):
        buttonClicked = self.playBtn.rect.collidepoint(mousePos)

        if buttonClicked and not self.gameActive:
            self.stats.resetStats()
            self.gameActive = True

            self.asteroids.empty()
            self.player.center()

            pg.mouse.set_visible(False)
                
    def _checkDownEvents(self, event):
        for event in pg.event.get():
            if event.key == pg.K_RIGHT:
                    self.player.moveRight = True
            elif event.key == pg.K_LEFT:
                self.player.moveLeft = True
            elif event.key == pg.K_UP:
                self.player.moveUp == True
            elif event.key == pg.K_DOWN:
                self.player.moveDown == True
            elif event.key == pg.K_q:
                sys.exit()

    def _checkUpEvents(self, event):
        if event.key == pg.K_RIGHT:
            self.player.moveRight == False
        elif event.key == pg.K_LEFT:
            self.player.moveLeft == False
        elif event.key == pg.K_UP:
            self.player.moveUp == False
        elif event.key == pg.K_DOWN:
            self.player.moveDown == False

    def _createAsteroids(self):
        asteroids = Asteroid(self)
        astWidth, astHeight = asteroids.rect.size

        currentX, currentY = astWidth, astHeight


    def _createAsteroid(self, xPos, yPos):
        newAst = Asteroid(self)
        newAst.x = xPos
        newAst.rect.x = xPos
        newAst.rect.y = yPos
        self.asteroids.add(newAst)

    def _checkAllEvents(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            elif e.type == pg.KEYDOWN:
                self._checkDownEvents(e)
            elif e.type == pg.KEYUP:
                self._checkUpEvents(e)
            elif e.type == pg.MOUSEBUTTONDOWN:
                mousePos = pg.mouse.get_pos()
                self._checkPlay(mousePos)

    def _update(self):
        self.screen.fill(self.settings.bgColor)

        self.player.draw()
        self.asteroids.draw(self.screen)

        if not self.gameActive:
            self.playBtn.draw()

        pg.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()    