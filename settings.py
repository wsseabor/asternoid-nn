from constants import *

class Settings():
    def __init__(self):
        self.screenWidth = SCREEN_X
        self.screenHeight = SCREEN_Y
        self.bgColor = BG_COLOR

        self.astLimit = 5

        self.astSpeed = 5

        self.speedScaling = 1.1

    def dynamicSettings(self):
        self.ShipSpeed = 1.5
        self.astSpeed = 1.0
        self.points = 0

    def increase(self):
        self.ShipSpeed += self.speedScaling
        self.astSpeed += self.speedScaling
        self.points += 1