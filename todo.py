import sys
import termios
import tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    todo_file = "todo.txt"
    tasks = []
    try:
        with open(todo_file, "r") as file:
            tasks = file.readlines()
        tasks = [task.rstrip() for task in tasks]
    except FileNotFoundError:
        open(todo_file, "w").close()
    
    while True:
        print("\033c", end="")
        print("Todo List:")
        for i, task in enumerate(tasks):
            print(f"{i}. [] {task}")
        print("")
        print("___________")
        print("")
        print("a: Add Task")
        print("r: Remove Task")
        print("q: Quit")
        choice = getch()
        if choice == 'a':
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == 'r':
            task_index = int(input("Enter task index: "))
            if task_index < len(tasks):
                tasks.pop(task_index)
        elif choice == 'q':
            break
        with open(todo_file, "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
main()