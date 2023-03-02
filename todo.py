import sys
import termios
import tty

# This function reads a single character of input from the user without waiting for a newline
def getch():
    # Get the file descriptor of the standard input stream
    fd = sys.stdin.fileno()
    # Save the current terminal settings
    old_settings = termios.tcgetattr(fd)
    try:
        # Set the terminal settings to raw mode, which disables line buffering and character echoing
        tty.setraw(sys.stdin.fileno())
        # Read a single character from the standard input stream
        ch = sys.stdin.read(1)
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    # Return the character that was read
    return ch

def main():
    # Set the filename for the to-do list
    todo_file = os.path.join(os.path.expanduser("~"), "Documents", "todo.txt")
    # Initialize the list of tasks to an empty list
    tasks = []
    try:
        # Try to open the to-do list file for reading
        with open(todo_file, "r") as file:
            # Read all the lines from the file into a list of strings
            tasks = file.readlines()
        # Remove any newline characters from the end of each task string
        tasks = [task.rstrip() for task in tasks]
    except FileNotFoundError:
        # If the to-do list file doesn't exist, create it
        open(todo_file, "w").close()
    
    # Enter a loop to display the to-do list and prompt the user for input
    while True:
        # Clear the terminal screen
        print("\033c", end="")
        # Print the header for the to-do list
        print("Todo List:")
        # Print each task in the list with an index number
        for i, task in enumerate(tasks):
            print(f"{i}. [] {task}")
        # Print some blank lines for spacing
        print("")
        print("___________")
        print("")
        # Print the menu of options
        print("a: Add Task")
        print("r: Remove Task")
        print("q: Quit")
        # Read a single character of input from the user
        choice = getch()
        # If the user chooses to add a task
        if choice == 'a':
            # Prompt the user to enter a new task and add it to the list
            task = input("Enter task: ")
            tasks.append(task)
        # If the user chooses to remove a task
        elif choice == 'r':
            # Prompt the user to enter the index of the task to remove and remove it from the list
            task_index = int(input("Enter task index: "))
            if task_index < len(tasks):
                tasks.pop(task_index)
        # If the user chooses to quit
        elif choice == 'q':
            # Clear the terminal screen
            print("\033c", end="")
            # Exit the loop
            break
        # Write the updated list of tasks to the to-do list file
        with open(todo_file, "w") as file:
            for task in tasks:
                file.write(f"{task}\n")

# Call the main function to run the program
main()
