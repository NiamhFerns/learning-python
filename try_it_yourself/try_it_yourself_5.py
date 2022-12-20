def hello_admin_E5_8():
    users = ["Steve", "Jerry", "Sarah", "Hannah", "admin"]
    for user in users:
        if user == "admin":
            print("Welcome back. For admin actions type 'sys --actions'.")
        else:
            print(f"Welcome back, {user}!")


def no_users_E5_9():
    users = ["Steve", "Jerry", "Sarah", "Hannah", "admin"]
    if not users:
        print("Sorry this list is empty.")
        return

    for user in users:
        if user == "admin":
            print("Welcome back. For admin actions type 'sys --actions'.")
        else:
            print(f"Welcome back, {user}!")


def checking_usernames_E5_10(users):
    users.sort()
    for i in range(len(users) - 1):
        if users[i].lower() == users[i + 1].lower():
            print(f"The user {users[i]} already exists in this database.", end=" ")
            print("Please pick a different name.")
            return

    print("All users are unique.")
