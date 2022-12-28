class Settings:
    """This is just a simple class that holds the settings for the session."""

    def __init__(self) -> None:
        """Set all the settings that we'll be using as an instance of settings.
        These are just defaults."""
        # Screen related.
        self.screen_dimension = (1200, 800)
        self.default_bg = (230, 230, 230)
        self.ship_speed = 2
        self.bullet_size = (7, 15)
        self.bullet_speed = 4
        self.bullet_colour = (255, 0, 255)
        self.max_bullet_count = 3
        self.max_alien_offset = 50
        self.alien_speed = 5
        self.aliens_x_count = 20
        self.aliens_y_count = 4
        self.aliens_x_gap = 20
        self.aliens_y_gap = 30
        self.aliens_w = 60
        self.aliens_h = 53
        self.max_lives = 3
