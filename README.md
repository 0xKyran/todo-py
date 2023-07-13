# TODO List CLI

A simple CLI to manage your tasks in any git repository.

## Table of Contents

- [Installation](#installation)
- [Building](#building)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

The TODO List CLI requires Python 3.6+ to run. Install the necessary dependencies and the application using the following commands:

Clone the repository to your local machine:
```bash
git clone https://github.com/0xKyran/todo-py.git
```

copy the `todo` file to your `/bin` directory:
```bash
sudo cp ./todo-py/bin/todo /bin
```

Or run todo.py directly:
```bash
python3 ./todo-py/src/todo.py
```

## building

To build the application, run the following command:

```bash
pyinstaller --onefile .//todo.py
```

## usage

This CLI can be used to manage tasks in any git repository. It stores the tasks in a file named TODO in the root of the repository.

To run the CLI, navigate to your git repository and execute the command:

```bash
todo
```

The following options are available:

- `a`: Add a new task.
- `r`: Remove an existing task.
- `d`: Mark a task as done.
- `q`: Quit the application.

## contributing

The project is opensource but not open for contributions. If you have any suggestions, please open an issue.

## license

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.