def city_name_E11_1(city, country):
    return f"{city.title()}, {country.title()}"


def city_name_E11_2(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()}, {population}"
    return f"{city.title()}, {country.title()}"


class Employee:
    def __init__(self, first_name, last_name, salary=45000) -> None:
        self.fname = first_name
        self.lname = last_name
        self.salary = salary

    def give_raise(self, custom=5000):
        self.salary += custom
