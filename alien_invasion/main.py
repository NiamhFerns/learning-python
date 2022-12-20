import sys
import pygame

from settings import Settings
from entity import IEntity
from ship import Ship
from bullet import Bullet
from keys import Keys


class AlienInvasion:
    """Overal class to manage game assets and behaviour."""

    def __init__(self) -> None:
        """Initialise the game and create game resources."""
        pygame.init()

        self.settings = Settings()

        # Window and panel settings.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_dimension = (
            self.screen.get_rect().w,
            self.screen.get_rect().h,
        )
        pygame.display.set_caption("Alien Invasion")

        # Set entities to load game with.
        self.entities: IEntity = []
        ship = Ship(self)
        self.entities.append(ship)

        self.keys = Keys()
        self.set_bindings(ship=ship)
        ship.speed = self.settings.ship_speed

    def set_bindings(self, **entities):
        """Sets all the bindings for things in the game. If binding is related to a
        specific entity, access entity via optional args."""
        self.keys.add_binding(
            pygame.K_RIGHT,
            lambda: entities["ship"].move_right(),
            lambda: entities["ship"].clear_movement(),
        )
        self.keys.add_binding(
            pygame.K_LEFT,
            lambda: entities["ship"].move_left(),
            lambda: entities["ship"].clear_movement(),
        )
        self.keys.add_binding(
            pygame.K_SPACE, lambda: Bullet.spawn(self)
        )

    def run(self):
        """Start the main loop for the game."""
        while True:
            self.find_events()
            self.call_game_tick()
            # THIS SHOULD ONLY BE CALLED WHEN TICK IS FINISHED.
            pygame.display.flip()

    def find_events(self):
        """Watch for events and perform the correct action when needed."""
        # Look for the correct course of action.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.keys.press(event.key)
                    continue
                self.keys.hold(event.key)
            elif event.type == pygame.KEYUP:
                self.keys.release(event.key)
        # Once the current keyboard state is known, apply all held keys.
        self.keys.apply_held()

    def call_game_tick(self):
        """Perform all actions needed after a cycle of the game's clock."""
        self.screen.fill(self.settings.default_bg)
        for entity in self.entities:
            if not isinstance(entity, IEntity):
                self.entities.remove(entity)
                continue
            entity.update()
            self.clear_unneeded()
            entity.draw()

    def clear_unneeded(self):
        """Remove an entity if it has requested deletion."""
        for entity in self.entities:
            if entity.remove:
                self.entities.remove(entity)


def main():
    game = AlienInvasion()
    game.run()


if __name__ == "__main__":
    main()
