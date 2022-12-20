from entity import IEntity
import pygame


class Bullet(IEntity):
    """This is the class responsible for representing a player's bullet."""

    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen
        self.speed = game.settings.bullet_speed
        self.colour = game.settings.bullet_colour
        self.dimensions = game.settings.bullet_size
        self.rect = pygame.Rect(0, 0, self.dimensions[0], self.dimensions[1])
        self.rect.midtop = game.entities[0].rect.midtop

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0 + self.dimensions[1]:
            self.remove = True

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
