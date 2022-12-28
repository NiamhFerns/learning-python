class GameStats():
    """This is a class to track all the statistics related to the player and the aliens."""
    def __init__(self, game) -> None:
        self.game = game
        self.lives = self.game.settings.max_lives

    def reset_stats(self):
        self.lives = self.game.settings.max_lives
