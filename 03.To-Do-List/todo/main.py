import argparse
from todo.utils import (
    list_todos,
    change_status,
    add_todo,
    delete_todo,
    menu,
    get_todos,
)  # Import necessary functions
import sys
from colorama import Style, Fore  # Import colorama for colored terminal output


def main():
    # Set up argument parser for command-line interface
    parser = argparse.ArgumentParser(description="A Simple CLI based todo application")
    parser.add_argument("--toggle", help="Toggle the todo to done or not done")
    parser.add_argument(
        "--delete",
        help="Delete the specific todo",
    )
    parser.add_argument("--new", help="Add a new todo")
    parser.add_argument("--list", help="List all the todos", action="store_true")

    # Parse the arguments provided by the user
    args = parser.parse_args()
    provided_args = sum(arg is not None for arg in vars(args).values())

    # Ensure only one argument is provided at a time
    if provided_args > 2:
        print("Error: Only one argument can be passed at a time.")
        sys.exit(1)

    # Handle toggling the status of a todo
    if args.toggle:
        change_status(args.toggle)

    # Handle deleting a todo
    elif args.delete:
        delete_todo(args.delete)

    # Handle adding a new todo
    elif args.new:
        if len(args.new) > 16:
            print(
                f"{Fore.RED}Error: Todo length should be less than 16 characters.{Style.RESET_ALL}"
            )
            sys.exit(1)
        todos = get_todos()
        for todo in todos:
            if todo["name"] == args.new:
                print(f"{Fore.RED}Error: Todo already exists.{Style.RESET_ALL}")
                sys.exit(1)
        desc = input(f"{Fore.CYAN}Enter the description of the todo: {Style.RESET_ALL}")
        if len(desc) > 50:
            print(
                f"{Fore.RED}Error: Description length should be less than 50 characters.{Style.RESET_ALL}"
            )
            sys.exit(1)
        add_todo(name=args.new, desc=desc, status=False)

    # Handle listing all todos
    elif args.list:
        list_todos()

    # Display the menu if no specific argument is provided
    else:
        menu()


# Entry point of the script
if __name__ == "__main__":
    main()
