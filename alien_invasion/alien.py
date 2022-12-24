import pygame

from entity import IEntity


class Alien(IEntity):
    # Static class containing all aliens currently in play.
    instances = []

    def __init__(self, game, starting_location) -> None:
        """Create an alien and give it a starting location."""
        super().__init__()
        self.screen = game.screen

        self.texture = pygame.image.load("textures/alien.png")
        self.rect = self.texture.get_rect()

        # Current location.
        self.rect.x = starting_location[0]
        self.rect.y = starting_location[1]

        self.min_x = self.rect.x
        self.max_x = self.rect.x + game.settings.max_alien_offset
        self.location_x = self.rect.x
        self.direction = 1
        self.speed = game.settings.alien_speed

    def build_fleet(game):
        """Builds a fleet of aliens."""
        for y in range(0, game.settings.aliens_y_count):
            for x in range(0, game.settings.aliens_x_count):
                Alien.instances.append(
                    Alien(
                        game,
                        (
                            x * (game.settings.aliens_x_gap + game.settings.aliens_w),
                            y * (game.settings.aliens_y_gap + game.settings.aliens_h),
                        ),
                    )
                )
        [game.entities.append(alien) for alien in Alien.instances]

    def move_down(self):
        self.rect.y += self.rect.h + 20

    def update(self):
        self.location_x += self.direction * self.speed
        self.rect.x = self.location_x
        if self.rect.x >= self.max_x or self.location_x <= self.min_x:
            self.direction *= -1
            self.move_down()
            if self.rect.y <= self.screen.h:
                self.remove = True

    def draw(self):
        self.screen.blit(self.texture, self.rect)

    def remove(self):
        super().remove()
        Alien.instances.remove(self)
