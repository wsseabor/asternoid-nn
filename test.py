#/usr/bin/env/python3

"""
Test file to get dimensons of image files
"""

import pygame as pg
import os
from PIL import Image
import os.path

os.environ['SDL_VIDEO_CENTERED'] = '1'

W = 800
H = 600

pg.init()
bg = pg.image.load("assets/stars_texture.png")
ast = pg.image.load("assets/asteroid.png")
win = pg.display.set_mode((W, H))
location = pg.math.Vector2(96, 96)
rect = pg.Rect(0, 64, 32, 64)


while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break
    win.fill((0, 0, 0))
    win.blit(bg, bg.get_rect(center = win.get_rect().center))
    win.blit(ast, ast.get_rect(center = win.get_rect().center))
    pg.display.update()

pg.quit()


filename = os.path.join('assets/stars_texture.png')
img = Image.open(filename)
w, h = img.size
print("Dimensons: ", img.size, "Total pixels: ", w * h)

f = os.path.join('assets/asteroid.png')
i = Image.open(f)
w, h = img.size
left = 5
top = h / 4
right = 164
bottom = 3 * h / 4
i = i.crop()

print("Dimensions: ", img.size, "Total pixels: ",  w * h )


pg.quit()

