# Imports
import random
import string
from colorama import Fore, Style
import argparse
import pyperclip


def include_characters() -> str:
    """
    Asks the user if they want to include characters in the password.
    """
    ask = input(
        f"{Fore.CYAN}Do You want to inclue special charachters other than the following{Fore.GREEN}(!@#$%^&*-_~+-=): {Style.RESET_ALL}(y/N)"
    )
    if ask.lower() == "y":
        characters = input(
            f"{Fore.CYAN}Enter Characters without space or comma: {Style.RESET_ALL}"
        )
        return characters
    return ""


# fucntion that returns the password
def generate_password(length: int, include_characters: str = "") -> string:

    # Define the characters that can be used in the password
    characters = (
        string.ascii_letters + string.digits + "!@#$%^&*-_~+-=" + include_characters
    )

    # Generate the password
    password = "".join(random.choice(characters) for _ in range(length))

    return password


# Function to get the desired password length from the user
def get_length() -> int:
    length = input(
        f"{Fore.CYAN}Number of Digits for the password {Fore.GREEN}(default:16): {Style.RESET_ALL}"
    )
    if length:
        try:
            length = int(length)
            if length < 8 or length > 32:
                print(
                    f"{Fore.RED}NOTE: {Fore.LIGHTRED_EX}Password length must be between 8 to 32 characters{Style.RESET_ALL}"
                )
                length = get_length()
        except:
            length = 16
        return length
    return 16


def main():
    parser = argparse.ArgumentParser(
        description="A script to Generate A strong password"
    )
    parser.add_argument(
        "--clip", action="store_true", help="Copy the provided text to the clipboard"
    )
    parser.add_argument(
        "--hide",
        action="store_true",
        help="Prevent Password from Displaying on Screen (only works with --clip)",
    )

    args = parser.parse_args()
    length = get_length()
    # Generate the password
    password = generate_password(length=length, include_characters=include_characters())
    if args.clip:
        pyperclip.copy(password)
        if args.hide:
            return
        print(f"Password copied to clipboard: {password}")
    else:
        print(f"Password: {password}")


if __name__ == "__main__":
    main()
