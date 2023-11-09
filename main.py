#/usr/bin/env/python3

import pygame as pg
import os
from constants import *
import random
import time
from settings import Settings

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game():
    def __init__(self):

        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
        self.settings.screenWidth = self.screen.get_rect().width
        self.settings.screenHeight = self.screen.get_rect().height

        pg.display.set_caption(WIN_TITLE)

        self.stats = Stats()
        self.player = Player(self)
        self.asteroids = pg.sprite.Group()


    def render(self):
        #Background
        self.window.fill((0, 0, 0))
        self.window.blit(bgTexture, bgTexture.get_rect(center = self.window.get_rect().center))

        for unit in self.gameState.units:
            pass

        pg.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.render()
            self.clock.tick(FPS)


game = Game()
game.run()
pg.quit()

    

#OLD
"""
#Unit superclass
class Unit():
    def __init__(self, state, position, tile):
        self.state = state
        self.position = position
        self.tile = tile

    def move(self, vector):
        raise NotImplementedError()

#Player class based on unit superclass
class Player(Unit):
    def move(self, vector):
        newPlayerPos = self.position + vector

        if newPlayerPos.x < 0 or newPlayerPos.x >= self.state.worldSize.x \
        or newPlayerPos.y < 0 or newPlayerPos.y >= self.state.worldSize.y:
            return
        
        for unit in self.state.units:
            if newPlayerPos == unit.position:
                return
            
        self.position = newPlayerPos

#Enemy class based on unit superclass
class Asteroid(Unit):
    def move(self, vector):
        newAstPos = self.position + vector

        if newAstPos.x < 0 or newAstPos.x >= self.state.worldSize.x:
            return
        
        for unit in self.state.units:
            if newAstPos == unit.position:
                return
            
        self.position = newAstPos
            

#Game state class, tracks movement and position
class State():
    def __init__(self):
        self.worldSize = pg.math.Vector2(16, 10)
        self.units = [
            Player(self, pg.math.Vector2(8, 8), pg.math.Vector2(1, 0)),
            Asteroid(self, pg.math.Vector2(10, 8), pg.math.Vector2(0, 2))
        ]

    def updatePlayer(self, movePlayerCommand):
        for unit in self.units:
            unit.move(movePlayerCommand)
        
    def populate(self):
        maxOnScreen = 6

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
        self.winTexture = pg.image.load('assets/stars_texture.png')
        self.astTexture = pg.image.load('assets/asteroid.png')

        #Set display and vectors
        windowSize = self.state.worldSize.elementwise() * self.cellSize
        self.window = pg.display.set_mode((int(windowSize.x), int(windowSize.y)))
        pg.display.set_caption(WIN_TITLE)
        self.moveCommand = pg.math.Vector2(0, 0)
        self.astCommand = pg.math.Vector2(0, 0)

        #Looping
        self.clock = pg.time.Clock()
        self.running = True

    def processInput(self):
        #Init as Vec2
        self.movePlayerCommand = pg.math.Vector2(0, 0)

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

    #Define some random asteroid movement
    def asteroidMovement(self, astCommand):
        astCommand = pg.math.Vector2(0, 0)

        astCommand.y += 0.1
    
    #Update movement
    def update(self):
        self.state.updatePlayer(self.movePlayerCommand)

    #Render images and background to window
    def renderUnit(self, unit):
        spritePoint = unit.position.elementwise() * self.cellSize
        texturePoint = unit.tile.elementwise() * self.cellSize
        textureRect = pg.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x), int(self.cellSize.y))
        self.window.blit(self.unitTexture, spritePoint, textureRect)
        self.window.blit(self.astTexture, spritePoint, textureRect)

    def render(self):
        #Background
        self.window.fill((0, 0, 0))
        self.window.blit(self.winTexture, self.winTexture.get_rect(center = self.window.get_rect().center))

        #The rest of them
        for unit in self.state.units:
            self.renderUnit(unit)

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
"""