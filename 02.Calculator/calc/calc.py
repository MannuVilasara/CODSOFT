# Imports
import typer
import inquirer
from colorama import Fore, Style
import pyfiglet
from time import sleep
from yaspin import yaspin
import os
import webbrowser

# creating a typer instance as variable `app`
app = typer.Typer()


# A function to get input
def get_input():
    """
    get user inputs
    """
    try:
        number = input(f"{Fore.YELLOW}❯ {Style.RESET_ALL}")
        if number == "q":
            print(f"{Fore.RED}Exiting...{Style.RESET_ALL}")
            sleep(1)
            os._exit(0)
        if number == "help":
            print(f"{Fore.GREEN}Created By gh/MannuVilasara {Style.RESET_ALL}")
            print("----------------------------------------------------------")
            print(f"{Fore.GREEN}Available commands: {Style.RESET_ALL}")
            print(f"{Fore.GREEN}q: Quit{Style.RESET_ALL}")
            print(f"{Fore.GREEN}gh: Open Github Repository{Style.RESET_ALL}")
            print(f"{Fore.GREEN}clear: clear the screen{Style.RESET_ALL}")
            print(f"{Fore.GREEN}help: Show available commands{Style.RESET_ALL}")
            get_input()
        if number == "gh":
            print(f"{Fore.GREEN}Opening GitHub...{Style.RESET_ALL}")
            webbrowser.get().open(url="https://github.com/MannuVilasara/CODSOFT")
            get_input()
        if number == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            get_input()
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

        os.system("cls" if os.name == "nt" else "clear")

        result = 0  # result
        typer.echo(f"{Fore.RED}Enter Integer to do calculations{Style.RESET_ALL}")
        number1 = get_input()  # getting number 1
        typer.echo(f"➥ {Fore.CYAN}{number1}{Style.RESET_ALL}")
        check = False
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
                        "Clear",
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
            elif action == "Clear":
                result = 0
                check = True
                
            if check == False:
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
                    os.system("cls" if os.name == "nt" else "clear")
                    typer.echo(
                        f"{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} Division by zero is not allowed."
                    )
                    continue
            
                

            os.system("cls" if os.name == "nt" else "clear")

            result = round(result, 2)
            typer.echo(f"❯ {Fore.GREEN}{result}{Style.RESET_ALL}")
            number1 = result  # update number1 to the result for the next operation
            check = False

    except KeyboardInterrupt:
        typer.echo(f"\n{Fore.RED}Cancelled by user.{Style.RESET_ALL}")


if __name__ == "__main__":
    app()
