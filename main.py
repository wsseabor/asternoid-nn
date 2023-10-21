#/usr/bin/env/python3

import pygame as pg
import os
from constants import *
import random
import time

os.environ['SDL_VIDEO_CENTERED'] = '1'

#Game state class, tracks movement and position
class State():
    def __init__(self):
        self.worldSize = pg.math.Vector2(16, 10)
        self.playerPos = pg.math.Vector2(8, 8)
        self.asteroidPos = []

    def update(self, moveCommand):
        self.playerPos += moveCommand

        if self.playerPos.x < 0:
            self.playerPos.x = 0
        elif self.playerPos.x >= self.worldSize.x:
            self.playerPos.x = self.worldSize.x - 1

        if self.playerPos.y < 0:
            self.playerPos.y = 0
        elif self.playerPos.y >= self.worldSize.y:
            self.playerPos.y = self.worldSize.y - 1

    def populate(self):
        maxOnScreen = 6

        while len(self.asteroidPos) <= maxOnScreen:
            self.asteroidPos.append(pg.math.Vector2(random.randint(0, 16), random.randint(0, 16)))
            for i in range(len(self.asteroidPos)):
                print(self.asteroidPos[i])



#Game class, primary event queue and loop
class Game():
    def __init__(self):

        #Required to run
        pg.init()

        #Init instance of game state
        self.state = State()

        #Calculate size of world and unit texture in img file, set window
        self.cellSize = pg.math.Vector2(UNIT_X, UNIT_Y)
        self.unitTexture = pg.image.load('assets/body_01.png')
        self.winTexture = pg.image.load("assets/stars_texture.png")

        windowSize = self.state.worldSize.elementwise() * self.cellSize
        self.window = pg.display.set_mode((int(windowSize.x), int(windowSize.y)))
        pg.display.set_caption(WIN_TITLE)
        self.moveCommand = pg.math.Vector2(0, 0)

        #Looping
        self.clock = pg.time.Clock()
        self.running = True


    def processInput(self):
        #Init as Vec2
        self.moveCommand = pg.math.Vector2(0, 0)

        #Event loop processing for movement input, using Vec2 in moveCommand tuple (x, y)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False
                break
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.running = False
                    break
                elif e.key == pg.K_RIGHT:
                    self.moveCommand.x = 1
                elif e.key == pg.K_LEFT:
                    self.moveCommand.x = -1
                elif e.key == pg.K_DOWN:
                    self.moveCommand.y = 1
                elif e.key == pg.K_UP:
                    self.moveCommand.y = -1
    
    #Update movement
    def update(self):
        self.state.update(self.moveCommand)

    #Render img and background to window
    def render(self):
        self.window.fill((0, 0, 0))
        
        spritePoint = self.state.playerPos.elementwise() * self.cellSize
        texturePoint = pg.math.Vector2(0, 0).elementwise() * self.cellSize
        textureRect = pg.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.winTexture, self.winTexture.get_rect(center = self.window.get_rect().center))
        self.window.blit(self.unitTexture, spritePoint, textureRect)

        self.state.populate()
        
        pg.display.update()

    #Loop
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

game = Game()
game.run()

pg.quit()