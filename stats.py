class Stats():
    def __init__(self, settings):
        self.settings = settings
        self.resetStats()

        self.gameActive= False

        self.highScore = 0

    def resetStats(self):
        self.score = 0
        self.highScore = self.highScore