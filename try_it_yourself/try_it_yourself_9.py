import random


class Restaurant_E9_1:
    """Initialises a restaurant and prints it's info."""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.type = cuisine_type
        self.open = False

    def describe_restaurant(self):
        if self.open:
            print(f"Welcome to {self.name}. Here we serve {self.type}")
        else:
            print(f"Sorry, but {self.name} is currently closed.")

    def open_restaurant(self):
        self.open = True

    def close_restaurant(self):
        self.open = False


def excercise_E9_2():
    rests = []
    rests.append(Restaurant_E9_1("Billy's Bakery", "Human Skin"))
    rests.append(Restaurant_E9_1("Sarah's Shacks", "The Souls of the Damned"))
    rests.append(Restaurant_E9_1("Satan's Sinful Sarlak Pit", "Brownies"))

    for item in rests:
        item.open_restaurant()
        item.describe_restaurant()


class User_E9_3:
    """This is a user."""

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = random.randint(0, 8092)

    def describe_user(self):
        print(f"Summary for user ID {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome, back.")


class Restaurant_E9_4:
    """Initialises a restaurant and prints it's info."""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.type = cuisine_type
        self.open = False
        self.served = 0

    def describe_restaurant(self):
        if self.open:
            print(f"Welcome to {self.name}. Here we serve {self.type}")
        else:
            print(f"Sorry, but {self.name} is currently closed.")

    def open_restaurant(self):
        self.open = True

    def close_restaurant(self):
        self.open = False

    def set_number_served(self, served):
        self.served = served

    def increment_number_served(self):
        self.served += 1


class User_E9_5:
    """This is a user."""

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = random.randint(0, 8092)
        self.login_attempts = 0

    def describe_user(self):
        print(f"Summary for user ID {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome, back.")

    def increment_login(self):
        self.login_attempts += 1

    def reset_attempts(self):
        self.login_attempts = 0


class IceCreamStand_E9_6(Restaurant_E9_4):
    """This is an icecream shop version of our restaurant."""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["chocolate", "vanilla", "sorbet", "caramel", "hazelnut"]

    def show_flavours(self):
        print("Avalable flavours include:")
        for flavour in self.flavours:
            print(f"\t{flavour}")


class Admin_E9_7(User_E9_5):
    """An admin is a subset of User."""

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.privileges = ["config", "settings", "networking", "partitioning"]

    def show_privileges(self):
        print("You have access to these additional privileges:")
        for p in self.privileges:
            print(f"\t{p.title()}")


class Admin_E9_8(User_E9_5):
    """An admin is a subset of User."""

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.privileges = Privileges_E9_8(
            "config", "settings", "networking", "partitioning"
        )

    def show_privileges(self):
        print("You have access to these additional privileges:")
        self.privileges.list_all()


class Privileges_E9_8:
    def __init__(self, *privileges) -> None:
        self.privileges = [p for p in privileges]

    def list_all(self):
        for p in self.privileges:
            print(f"\t{p}")


"""
Excerises 9-9 through 9-16 were just repeats of stuff I've already been doing.
"""
