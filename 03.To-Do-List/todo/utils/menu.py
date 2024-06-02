from todo.utils import (
    get_input,
    list_todos,
)  # Importing functions from the utils module
from todo.utils import show_logo  # Importing show_logo function from the utils module
import os
from time import sleep  # Importing sleep function to pause the execution
from yaspin import yaspin  # Importing yaspin for spinner animations
import inquirer  # Importing inquirer for interactive command line prompts
from colorama import Fore, Style  # Importing colorama for colored terminal output


# Function to display the main menu and handle user actions
def menu():
    show_logo()  # Display the logo
    spinner = yaspin()
    # Start and stop the spinner to show the logo
    spinner.start()
    sleep(1)
    spinner.stop()
    while True:
        # Clear the terminal screen
        os.system("cls" if os.name == "nt" else "clear")
        list_todos()  # Display the list of todos
        # Define the list of actions for the user to choose from
        questions = [
            inquirer.List(
                "action",
                message="Choose Action",
                choices=[
                    "New",
                    "Delete",
                    "toggle",
                    "Exit (q)",
                ],
            )
        ]
        # Prompt the user to choose an action
        action_response = inquirer.prompt(questions)
        # Handle the user's choice
        if action_response["action"] == "New":
            get_input(1)  # Get input for adding a new todo
        elif action_response["action"] == "Delete":
            get_input(2)  # Get input for deleting a todo
        elif action_response["action"] == "toggle":
            get_input(3)  # Get input for toggling the status of a todo
        elif action_response["action"] == "Exit (q)":
            print(f"{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
            exit()  # Exit the program
        else:
            print("Invalid choice")  # Handle invalid choices
