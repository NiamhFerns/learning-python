class Settings:
    """This is just a simple class that holds the settings for the session."""

    def __init__(self) -> None:
        """Set all the settings that we'll be using as an instance of settings.
        These are just defaults."""
        # Screen related.
        self.screen_dimension = (1200, 800)
        self.default_bg = (230, 230, 230)
        self.ship_speed = 1
        self.bullet_size = (4, 10)
        self.bullet_speed = 2
        self.bullet_colour = (255, 0, 0)
