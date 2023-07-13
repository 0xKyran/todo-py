import sys
import termios
import tty
import os
import json

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def print_menu():
    print("\n=========================================")
    print("TODO List")
    print("=========================================")

def print_tasks(tasks):
    for i, task in enumerate(tasks):
        check = '[x]' if task['done'] else '[ ]'
        print(f"{i+1}. {check} {task['name']}")
    print("")

def print_options():
    print("\nActions:")
    print("a: Add Task")
    print("r: Remove Task")
    print("d: Done Task")
    print("q: Quit")
    print("\n=========================================")

def main():
    if not os.path.isdir(".git"):
        print("Error: Not a git repository")
        return

    todo_file = "TODO"
    tasks = []
    try:
        with open(todo_file, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    except FileNotFoundError:
        open(todo_file, "w").close()

    while True:
        print("\033c", end="")
        print_menu()
        print_tasks(tasks)
        print_options()
        choice = getch()

        if choice == 'a':
            task_name = input("Enter task: ")
            tasks.append({'name': task_name, 'done': False})
        elif choice == 'r':
            task_index = int(input("Enter task index: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
        elif choice == 'd':
            task_index = int(input("Enter task index to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]['done'] = True
        elif choice == 'q':
            print("\033c", end="")
            break

        with open(todo_file, "w") as file:
            json.dump(tasks, file)

if __name__ == "__main__":
    main()
