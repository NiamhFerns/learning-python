import pygame
from pygame.sprite import Sprite

from entity import IEntity
from bullet import Bullet


class Alien(IEntity, Sprite):
    # Static class containing all aliens currently in play.
    instances = pygame.sprite.Group()

    def __init__(self, game, starting_location) -> None:
        """Create an alien and give it a starting location."""
        IEntity.__init__(self)
        Sprite.__init__(self)
        self.screen = game.screen
        Alien.game = game

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
        """Builds a fleet of aliens at the start of a game/round."""
        for bullet in Bullet.instances:
            Bullet.remove(bullet)

        for y in range(0, game.settings.aliens_y_count):
            for x in range(0, game.settings.aliens_x_count):
                alien = Alien(
                    game,
                    (
                        x * (game.settings.aliens_x_gap + game.settings.aliens_w),
                        y * (game.settings.aliens_y_gap + game.settings.aliens_h),
                    ),
                )
                Alien.instances.add(alien)
                game.entities.append(alien)

    def force_clear_instances():
        """Forcibly clears instances from the game without waiting on a cycle."""
        for instance in Alien.instances:
            Alien.remove(instance)
            Alien.game.entities.remove(instance)

    def move_down(self):
        """Moves the fleet of aliens down a line."""
        self.rect.y += self.rect.h + 20

    def update(self):
        self.location_x += self.direction * self.speed
        self.rect.x = self.location_x
        if self.rect.x >= self.max_x or self.location_x <= self.min_x:
            self.direction *= -1
            self.move_down()
            if self.rect.y + self.rect.h >= self.screen.get_rect().h:
                self.remove = True

    def draw(self):
        self.screen.blit(self.texture, self.rect)

    @staticmethod
    def remove(entity):
        super().remove(entity)
        Alien.instances.remove(entity)
