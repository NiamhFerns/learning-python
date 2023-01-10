class GameStats():
    """This is a class to track all the statistics related to the player and the aliens."""
    def __init__(self, game) -> None:
        self.game = game
        self.lives = self.game.settings.max_lives
        self.current_score = 0

    def score(self):
        self.current_score += 1

    def reset_stats(self):
        self.lives = self.game.settings.max_lives
