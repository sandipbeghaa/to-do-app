import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")

def mark_done(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked '{tasks[index]['title']}' as done.")
    except IndexError:
        print("Invalid task number.")

def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        cmd = input("\nCommand [list/add/done/del/quit]: ").strip().lower()
        if cmd == "list":
            list_tasks(tasks)
        elif cmd.startswith("add"):
            title = cmd[4:] or input("Task: ")
            add_task(tasks, title)
        elif cmd.startswith("done"):
            idx = int(cmd[5:] or input("Task number: ")) - 1
            mark_done(tasks, idx)
        elif cmd.startswith("del"):
            idx = int(cmd[4:] or input("Task number: ")) - 1
            delete_task(tasks, idx)
        elif cmd == "quit":
            break
        else:
            print("Unknown command. Try list/add/done/del/quit.")

if __name__ == "__main__":
    main()
