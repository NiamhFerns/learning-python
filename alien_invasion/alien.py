import pygame

from entity import IEntity


class Alien(IEntity):
    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.screen

        self.texture = pygame.image.load("textures/alien.png")
        self.rect = self.texture.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.texture, self.rect)
