import json


def print_lines_E10_1():
    with open("example_text.txt") as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())


def print_replaced_lines_E10_2(word, replacement):
    with open("example_text.txt") as file:
        lines = file.readlines()

    for line in lines:
        print(line.replace(word, replacement).strip())


def prompt_write_E10_3():
    name = input("Please enter your name: ")
    with open("text_out.txt", "w") as out_stream:
        out_stream.writelines(name)


def write_gues_book_E10_4():
    name = ""
    with open("text_out.txt", "w") as out_stream:
        name = input("Add guest: ")
        while name.upper() != "QUIT":
            out_stream.write(name + "\n")
            name = input("Add guest: ")


"""Excercise 10-5 is a repeat of 10-4."""


def catch_value_error_E10_6():
    try:
        num1 = int(input("Enter the first operator: "))
        num2 = int(input("Enter the second operator: "))

        print(f"The result is {num1 + num2}.")
    except ValueError:
        print("One of the numbers you entered is incorrect. Please retry.")


"""Excercise 10-7 is a repeat of 10-6 with a while loop."""


"""Excercise 10-8 is 10-5 + 10-7. Catches FileNotFound error."""


"""Excercise 10-9 is 10-8 with a pass in the except block."""


"""Excercise 10-10 is just count on a file read."""


def write_number_E10_11():
    try:
        num = int(input("What's your favourite number? "))

        with open("json_out.json", "w") as out_stream:
            json.dump(num, out_stream)
    except ValueError:
        print("That's not a valid number, sorry.")


def read_number_E10_11():
    try:
        with open("json_out.json", "r") as in_stream:
            num = json.load(in_stream)

        print(f"Hey... I know your number now. It's {num}")
    except UnboundLocalError:
        pass
    except json.decoder.JSONDecodeError:
        pass


"""Excercise 10-12 is a repeat of 10-11."""


"""Excercise 10-13 is a repeat of 10-11 with verification."""
