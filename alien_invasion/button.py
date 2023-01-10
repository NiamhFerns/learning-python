import pygame
import pygame.font


class Button:
    """Responsible for being a button."""

    def __init__(self, game, txt) -> None:
        self.screen = game.screen
        self.game = game

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen.get_rect().center

        self._prep_msg(txt)

    def _prep_msg(self, txt):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(txt, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw our button to the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
