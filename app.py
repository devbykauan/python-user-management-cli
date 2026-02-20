from storage import load_data
from menu import run_menu


def main() -> None:
    users = load_data()
    run_menu(users)


if __name__ == "__main__":
    main()
