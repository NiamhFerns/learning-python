def person_E6_1():
    person_dict = {
        "first_name": "Niamh",
        "last_name": "Ferns",
        "age": 22,
        "address": "47c Tennyson Avenue, Avalon, Lower Hutt, 5011",
    }

    for key, value in person_dict.items():
        print(f"This person's {key.replace('_', ' ').title()} is {value}.")


def people_E6_7(template_dict):
    people_list = []
    try:
        for i in range(0, 10):
            dict = {}
            for key, val in template_dict.items():
                dict[key] = str(val) + str(i)
            people_list.append(dict)
        return people_list
    except Exception:
        print("Sorry, that isn't a valid template.")
