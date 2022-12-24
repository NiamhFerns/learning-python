class IEntity:
    """This is an interface class that just makes sure there objects
    can act like an entity."""
    def __init__(self) -> None:
        self.remove = False

    def update(self):
        pass

    def draw(self):
        pass

    def remove(self):
        self.remove = True
