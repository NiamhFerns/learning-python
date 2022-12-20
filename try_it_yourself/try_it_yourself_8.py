def display_message_E8_1():
    print("I'm learning about functions/routines in this chapter.")


def favourite_book_E8_2(title):
    if not isinstance(title, str):
        print("That is not a valid argument. Try again.")
        return

    print(f"One of my favourite books is {title}.")


def make_shirt_E8_3(size, text):
    print(f"Thank you for ordering a new size {size} t-shirt. Your text is '{text}'.")


def make_shirt_E8_4(size="LARGE", text="Caption Here"):
    print(f"Thank you for ordering a new size {size} t-shirt. Your text is '{text}'.")


def describe_city_E8_5(city="Wellington", country="New Zealand"):
    print(f"The {city} city is located in {country}.")


def city_country_E8_6(city, country):
    return f"{city.title()}, {country.title()}"


def make_album_E8_7(artist, title, song_count=None):
    pass


def make_album_E8_8():
    pass


def show_messages_E8_9(messages):
    pass


def send_messages_E8_10(messages):
    pass


def send_messages_E8_11(messages):
    pass


def sandwiches_E8_12(*ingredients):
    print("Thank you for ordering from us.\n\tConfirmation of order:")
    print("\tPlain Bread\n\tSalt\n\tPepper")
    for ingredient in ingredients:
        print("\t" + ingredient.title())


def build_profile_E8_13(first, last, **details):
    details["first"] = first
    details["last"] = last
    return details


def make_car_E8_14(manufacturer, model, **details):
    pass


"""
8-15 and 8-16 are about imports and weren't included here because it's obvious.
Anything with pass was repeated or obvious.
"""


def main():
    pass


main()
