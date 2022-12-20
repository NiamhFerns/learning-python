import pygame
import sys
import types


class Keys:
    """This is the class that handles the keypresses used in a game."""

    def __init__(self) -> None:
        self.map = {}
        # Default bindings.
        self.add_binding(pygame.K_ESCAPE, lambda: sys.exit())

    def add_binding(self, key: int, mapping, clear=None):
        """Add a binding to the map."""
        if not isinstance(mapping, types.LambdaType):
            raise TypeError(
                f"Type of {type(mapping)} is incorrect. Should be of type {type(types.LambdaType)}."  # noqa: E501
            )
        self.map[key] = {"held": False, "action": mapping, "clear": clear, "reset_requested": False}

    def press(self, key: int):
        """Applies a binding only once."""
        if not self.map.get(key) is None:
            self.map.get(key)["action"]()

    def hold(self, key: int):
        """Set the held flag to true so that this key is repeatedly applied each tick."""
        if not self.map.get(key) is None:
            self.map.get(key)["held"] = True

    def release(self, key: int):
        """Set the held flag to false so that this key is no longer applied each tick."""
        if not self.map.get(key) is None:
            self.map.get(key)["held"] = False
            self.map.get(key)["reset_requested"] = True

    def clear(self, key: int):
        """Clear the binding if it has clear code available"""
        if (not self.map.get(key) is None) and self.map.get(key)["clear"]:
            self.map.get(key)["clear"]()
            self.map.get(key)["reset_requested"] = False

    def apply_held(self):
        """Apply all bindings in the map that are held."""
        for key, binding in self.map.items():
            if binding["held"]:
                self.press(key)
            elif not binding["held"] and binding["reset_requested"]:
                self.clear(key)
