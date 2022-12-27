class IEntity:
    """This is an interface class that just makes sure there objects
    can act like an entity."""
    def __init__(self) -> None:
        self.remove = False

    def update(self):
        pass

    def draw(self):
        pass

    @staticmethod
    def remove(entity):
        entity.remove = True
