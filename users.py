from storage import save_data


def create_user(users: list[dict]) -> None:
    name = input("\nEnter name: ").strip().title()

    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Enter a valid age.")
            else:
                break
        except ValueError:
            print("Enter a valid number.")

    users.append({"name": name, "age": age})
    save_data(users)
    print("User created successfully!\n")


def list_users(users: list[dict]) -> None:
    if not users:
        print("\nNo users found.\n")
        return

    print("\n=== Users List ===")
    for i, user in enumerate(users, start=1):
        print(f"{i}. Name: {user['name']} | Age: {user['age']}")
    print()


def update_user(users: list[dict]) -> None:
    if not users:
        print("\nNo users found.\n")
        return

    list_users(users)

    while True:
        try:
            index = int(input("Enter user number to update: ")) - 1

            if 0 <= index < len(users):
                new_name = input("New name: ").strip().title()

                while True:
                    try:
                        new_age = int(input("New age: "))
                        if new_age <= 0:
                            print("Enter a valid age.")
                        else:
                            break
                    except ValueError:
                        print("Enter a valid number.")

                users[index]["name"] = new_name
                users[index]["age"] = new_age

                save_data(users)
                print("User updated successfully!\n")
                break
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")


def delete_user(users: list[dict]) -> None:
    if not users:
        print("\nNo users found.\n")
        return

    list_users(users)

    while True:
        try:
            index = int(input("Enter user number to delete: ")) - 1

            if 0 <= index < len(users):
                user = users[index]
                confirm = input(
                    f"Are you sure you want to delete {user['name']}? (y/n): "
                ).strip().lower()

                if confirm == "y":
                    users.pop(index)
                    save_data(users)
                    print("User deleted successfully!\n")
                else:
                    print("Operation cancelled.\n")
                break
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")
