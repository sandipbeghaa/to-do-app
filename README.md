# Terminal To-Do App

A simple command-line to-do list written in Python. You can add, view, complete, and delete tasks right from your terminal, and everything saves automatically to a local `tasks.json` file so your list is still there next time you run it.

## What It Does

- **View Tasks (`list`):** Shows your numbered task list with a checkmark (`✓`) next to finished items.
- **Add Tasks (`add`):** Add a task directly (like `add Buy milk`) or type `add` and enter the title when prompted.
- **Mark Tasks Done (`done`):** Mark any task complete by its number (like `done 1`).
- **Delete Tasks (`del`):** Remove a task from your list by its number (like `del 2`).
- **Automatic Saving:** Uses Python's `json` and `pathlib` modules to save every change to `tasks.json` automatically.

## Built With

- Python 3
- Python Standard Library (`json` and `pathlib`)

## Project Structure

```text
to-do-app/
├── todo_list.py
└── README.md
```

*(Note: `tasks.json` is created automatically in the same folder the first time you add a task.)*

## How to Run It

1. Make sure **Python 3** is installed on your computer.
2. Clone or download this repository:
   ```bash
   git clone https://github.com/sandipbeghaa/to-do-app
   ```
3. Open the folder and run the script:
   ```bash
   cd to-do-app
   python to_do.py
   ```

## Example Usage

```text
Command [list/add/done/del/quit]: add Finish portfolio README
Added: Finish portfolio README

Command [list/add/done/del/quit]: list
1. [ ] Finish portfolio README

Command [list/add/done/del/quit]: done 1
Marked 'Finish portfolio README' as done.

Command [list/add/done/del/quit]: list
1. [✓] Finish portfolio README
```

## What I Practiced & Learned

- Using `pathlib.Path` to check for and manage a local JSON data file cleanly.
- Handling user commands and inline arguments (like `add <task>` or `done <number>`) inside a `while` loop.
- Catching `IndexError` exceptions so typing an invalid task number prints a helpful message instead of crashing the program.

## Author

- **GitHub:** [github.com/sandipbeghaa](https://github.com/sandipbeghaa)
- **Portfolio:** [sandipbeghaa.github.io](https://sandipbeghaa.github.io/)
