# 🔐 passgen: A simple cli based password generator

> NOTE: This is my project done for internship.

```bash
❯ passgen -h
usage: passgen [-h] [--clip] [--hide]

A script to Generate A strong password

options:
  -h, --help  show this help message and exit
  --clip      Copy the provided text to the clipboard
  --hide      Prevent Password from Displaying on Screen (only works with --clip)
```

## Feature:

- Generates strong and unique passwords
- User can choose the length of the password
- User can choose to add custom characters in password
- User can copy the generated password to clipboard with --clip
- User can hide the password with --hide while using with --clip option

## Tech Used:

- colorama: For showing coloured outputs
- pyperclip: to copy password to clipboard
- argparse: to get arguments

⭐ Star the repo :)
