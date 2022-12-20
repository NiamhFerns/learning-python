def name_cases_E2_4():
    upper = "Print this in Uppercase only."
    title = "Print this in Title-Case only."
    lower = "Print this in Lowercase only."
    print(f"This ins in uppercase: {upper.upper()}")
    print(f"This ins in lowercase: {lower.lower()}")
    print(f"This ins in title-case: {title.title()}")


def stripping_names_E2_7():
    name = "  this is a name with some trailing and leading white space\t\t\n "
    print(f"This is without stripping: {name}")
    print(f"This is with stripping: {name.lstrip().rstrip()}")
    print(f"This is with stripping with a single command: {name.strip()}")
