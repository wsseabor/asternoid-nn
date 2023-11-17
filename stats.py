class Stats():
    def __init__(self, game):
        self.settings = game.settings
        self.resetStats()

        self.highScore = 0

    def resetStats(self):
        self.score = 0