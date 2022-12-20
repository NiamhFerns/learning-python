import sys
import pygame


class game_E12_1:
    """Our game."""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))

        pygame.display.set_caption("My Game")
        self.man = game_E12_2(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((230, 230, 230))
            self.man.draw_me()
            pygame.display.flip()


class game_E12_2:
    """Draw a character to the screen."""

    def __init__(self, game) -> None:
        self.sprite = pygame.image.load("textures/man.png")
        self.rect = self.sprite.get_rect()
        self.screen = game.screen

    def draw_me(self):
        self.screen.blit(self.sprite, self.rect)


def main():
    game = game_E12_1()
    game.run()


if __name__ == "__main__":
    main()
