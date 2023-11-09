import sys
from time import sleep
import pygame as pg

from asteroid import Asteroid

def checkDownEvents(event, settings, screen, player):
    if event.key == pg.K_RIGHT:
        player.moveRight = True
    elif event.key == pg.K_LEFT:
        player.moveLeft = True
    elif event.key == pg.K_UP:
        player.moveUp == True
    elif event.key == pg.K_DOWN:
        player.moveDown == True
    elif event.key == pg.K_q:
        sys.exit()

def checkUpEvents(event, player):
    if event.key == pg.K_RIGHT:
        player.moveRight == False
    elif event.key == pg.K_LEFT:
        player.moveLeft == False
    elif event.key == pg.K_UP:
        player.moveUp == False
    elif event.key == pg.K_DOWN:
        player.moveDown == False

def checkAllEvents(settings, screen, stats, scoreboard, play, player, asteroids):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.KEYDOWN:
            checkDownEvents(e, settings, screen, player)
        elif e.type == pg.KEYUP:
            checkUpEvents(e, player)
        elif e.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            checkPlay()

def checkPlay(settings, screen, stats, scoreboard, play, player, asteroids, mouse_x, mouse_y):
    buttonClicked = play.rect.collidepoint(mouse_x, mouse_y)

    if buttonClicked and not stats.gameActive:
        settings.dyanmicSettings()

        pg.mouse.set_visible(False)

        stats.resetStats()
        stats.gameActive = True

        

        
