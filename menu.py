from users import create_user, list_users, update_user, delete_user


def run_menu(users: list[dict]) -> None:
    while True:
        print("=== MENU ===")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Update user")
        print("4 - Delete user")
        print("5 - Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            create_user(users)
        elif option == "2":
            list_users(users)
        elif option == "3":
            update_user(users)
        elif option == "4":
            delete_user(users)
        elif option == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option.\n")
