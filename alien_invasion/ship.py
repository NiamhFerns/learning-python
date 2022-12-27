import pygame
from pygame.sprite import Sprite

from entity import IEntity


class Ship(IEntity, Sprite):
    """A class to manage the ship."""

    instance = None

    def __init__(self, game) -> None:
        """Initialise the ship and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.speed = 1
        self.velocity_x = 0

        # Load the ship image and get its rect.
        self.image = pygame.image.load("textures/ship.png")
        self.rect = self.image.get_rect()

        # Start new ships in the bottom middle of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def take_damage(self):
        pass

    def update(self):
        if (
            not self.rect.x + self.velocity_x > (self.screen_rect.w - self.rect.w)
            and not self.rect.x + self.velocity_x < 0
        ):
            self.rect.x += self.velocity_x

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def move_right(self):
        """Set the velocity of the ship to move right."""
        self.velocity_x = self.speed

    def move_left(self):
        """Set the velocity of the ship to move left."""
        self.velocity_x = -self.speed

    def clear_movement(self):
        """Reset all velocities to 0."""
        self.velocity_x = 0
