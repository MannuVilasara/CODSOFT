# Imports
import inquirer.themes
import typer
import inquirer
from colorama import Fore, Style
import pyfiglet
from time import sleep
from yaspin import yaspin
import os

# creating a typer instance as variable `app`
app = typer.Typer()


# A function to get input
def get_input():
    """
    get user inputs
    """
    try:
        number = input(f"{Fore.YELLOW}❯ {Style.RESET_ALL}")
        try:
            number = int(number)
        except:
            number = float(number)
        return number
    except ValueError:
        typer.echo(
            f"{Fore.RED}Invalid input for number. Please enter a valid integer.{Style.RESET_ALL}"
        )
        return get_input()


# Main entrypoint function
@app.command()
def main():
    """
    A simple cli based calculator for calculations
    """
    try:
        # Display welcome message
        welcome_message = pyfiglet.figlet_format("CLI Calculator")
        typer.echo(f"{Fore.CYAN}{welcome_message}{Style.RESET_ALL}")

        spinner = yaspin()
        spinner.start()
        sleep(2)
        spinner.stop()

        os.system("clear")

        result = 0  # result
        number1 = get_input()  # getting number 1
        typer.echo(f"➥ {Fore.CYAN}{number1}{Style.RESET_ALL}")

        while True:
            # prompt list for options
            questions = [
                inquirer.List(
                    "action",
                    message="Choose Action",
                    choices=[
                        "Add (+)",
                        "Subtract (-)",
                        "Multiply (*)",
                        "Divide (/)",
                        "Exit (q)",
                    ],
                )
            ]
            action_response = inquirer.prompt(questions)
            if action_response is None:
                typer.echo(f"{Fore.RED}Cancelled by user.{Style.RESET_ALL}")
                break

            action = action_response["action"]
            typer.echo(f"Action chosen: {Fore.YELLOW}{action}{Style.RESET_ALL}")
            if action == "Exit (q)":
                typer.echo(
                    f"{Fore.CYAN}Exiting the calculator. Goodbye!{Style.RESET_ALL}"
                )
                break

            number2 = get_input()  # Getting number 2
            typer.echo(f"❯ {Fore.CYAN}{number2}{Style.RESET_ALL}")

            if action == "Add (+)":
                result = number1 + number2
            elif action == "Subtract (-)":
                result = number1 - number2
            elif action == "Multiply (*)":
                result = number1 * number2
            elif action == "Divide (/)":
                if number2 != 0:
                    result = number1 / number2
                else:
                    os.system("clear")
                    typer.echo(
                        f"{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} Division by zero is not allowed."
                    )
                    continue

            os.system("clear")
            
            result = round(result, 2)
            typer.echo(f"❯ {Fore.GREEN}{result}{Style.RESET_ALL}")
            number1 = result  # update number1 to the result for the next operation

    except KeyboardInterrupt:
        typer.echo(f"\n{Fore.RED}Cancelled by user.{Style.RESET_ALL}")


if __name__ == "__main__":
    app()
