# 🖋️ todo: A simple cli based to-do list

> NOTE: This is my project done for internship.

```bash
❯ todo -h
usage: todo [-h] [--toggle TOGGLE] [--delete DELETE] [--new NEW] [--list]

A Simple cli based todo applications

options:
  -h, --help       show this help message and exit
  --toggle TOGGLE  toggle the todo to done or not done
  --delete DELETE  Delete the specific todo
  --new NEW        Add a new todo
  --list           List all the todos

```

```bash
+--------+--------------------------+------------+----------+
| name   | desc                     | date       | status   |
+========+==========================+============+==========+
| mannu  | water plants             | 02/06/2024 | ✘        |
+--------+--------------------------+------------+----------+
| code   | write code to internship | 02/06/2024 | ✘        |
+--------+--------------------------+------------+----------+
[?] Choose Action:
 > New
   Delete
   toggle
   Exit (q)

```

## Feature:

- Add task
- Delete task
- Mark task as completed
- List all tasks

## Tech Used:

- colorama: For showing coloured outputs
- argparse: To get arguments
- inquirer: For interactive menu
- pyfiglet: For Showing Starting logo
- tabulate: To show todos in Table
- yaspin: For loading animation (this does nothing honestly but still gotta mention)

⭐ Star the repo :)
