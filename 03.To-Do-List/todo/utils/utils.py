import json
from datetime import date
from tabulate import tabulate  # Library for displaying tabular data in formatted tables
from colorama import init, Fore, Style  # Libraries for colored text in the terminal
import pyfiglet  # Library for creating ASCII art text
import sys
import os

# Initialize colorama for colored terminal output
init()

# Constant for handling not found cases
not_found = "not-found"


# Function to get the list of todos from a JSON file
def get_todos() -> list:
    try:
        # Open and read todos from the JSON file
        with open(os.path.expanduser("~/.todos.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Return an empty list if the file doesn't exist
        return []


# Function to update the todos in the JSON file
def update_todos(todos):
    with open(os.path.expanduser("~/.todos.json"), "w") as f:
        # Write the todos list to the file in JSON format
        json.dump(todos, f, indent=4)


# Function to add a new todo
def add_todo(name: str, status: bool, desc: str):
    todos = get_todos()
    # Limit the number of todos to 20
    if len(todos) >= 20:
        print(Fore.RED + "You can only add 20 todos." + Style.RESET_ALL)
        return
    # Create a new todo dictionary
    new_todo = {
        "name": name,
        "desc": desc,
        "date": date.today().strftime("%d/%m/%Y"),
        "status": status,
    }
    todos.append(new_todo)
    update_todos(todos)
    print(Fore.GREEN + f"Todo '{name}' added successfully!" + Style.RESET_ALL)


# Function to delete a todo by name
def delete_todo(name):
    todos = get_todos()
    for todo in todos:
        if todo["name"] == name:
            todos.remove(todo)
            update_todos(todos)
            print(Fore.GREEN + f"Todo '{name}' deleted successfully." + Style.RESET_ALL)
            return
    print(Fore.RED + f"Todo '{name}' not found." + Style.RESET_ALL)
    return not_found


# Function to change the status of a todo by name
def change_status(name):
    todos = get_todos()
    for todo in todos:
        if todo["name"] == name:
            # Toggle the status of the todo
            todo["status"] = not todo["status"]
            update_todos(todos)
            print(
                Fore.GREEN
                + f"Todo '{name}' status changed successfully."
                + Style.RESET_ALL
            )
            return
    print(Fore.RED + f"Todo '{name}' not found." + Style.RESET_ALL)
    return not_found


# Function to display the logo using ASCII art
def show_logo():
    result = pyfiglet.figlet_format("Todo List")
    print(Fore.CYAN + result + Style.RESET_ALL)


# Function to list all todos in a formatted table
def list_todos():
    todos = get_todos()
    if not todos:
        print(
            Fore.YELLOW
            + "No todos found. \n Add some todos to show here"
            + Style.RESET_ALL
        )
        return

    headers = todos[0].keys()
    rows = [
        [
            Fore.CYAN + str(todo["name"]) + Style.RESET_ALL,
            Fore.YELLOW + str(todo["desc"]) + Style.RESET_ALL,
            Fore.CYAN + str(todo["date"]) + Style.RESET_ALL,
            (
                (Fore.GREEN if todo["status"] else Fore.RED) + "✔"
                if todo["status"] == True
                else "✘" + Style.RESET_ALL
            ),
        ]
        for todo in todos
    ]
    print(tabulate(rows, headers, tablefmt="grid"))


# Function to get user input for different operations
def get_input(type: int):
    if type == 1:
        todos = get_todos()
        name = input(f"{Fore.CYAN}Enter the name of the todo: {Style.RESET_ALL}")
        for todo in todos:
            if name == todo["name"]:
                print(
                    Fore.RED + "Todo with same name already exists." + Style.RESET_ALL
                )
                input("Enter to Continue")
                return
        if len(name) > 16:
            print(
                f"{Fore.RED}Error: Todo length should be less than 16 characters.{Style.RESET_ALL}"
            )
            sys.exit(1)
        desc = input(f"{Fore.CYAN}Enter the description of the todo: {Style.RESET_ALL}")
        if len(desc) > 50:
            print(
                f"{Fore.RED}Error: Description length should be less than 50 characters.{Style.RESET_ALL}"
            )
            sys.exit(1)
        add_todo(name=name, desc=desc, status=False)
    elif type == 2:
        name = input(
            f"{Fore.RED}Enter the name of the todo to delete: {Style.RESET_ALL}"
        )
        delete_todo(name)
    elif type == 3:
        name = input(
            f"{Fore.GREEN}Enter the name of the todo to toggle: {Style.RESET_ALL}"
        )
        change_status(name)
    else:
        print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
