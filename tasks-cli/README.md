# Task Tracker CLI
Hello, world!
Task tracker is a project used to track and manage your tasks. It is a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.
This tool was created utilizing the <b>python3 standard library</b>.

## Prerequisites
- python3 >= 3.12.0
- cloned verison of this repository

## Usage
```
zsh

# Adding a new task
python3 task-cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python3 task-cli.py update 1 "Buy groceries and cook dinner"
python3 task-cli.py delete 1

# Marking a task as in progress or done
python3 task-cli.py mark-in-progress 1
python3 task-cli.py mark-done 1

# Listing all tasks
python3 task-cli.py list

# Listing tasks by status
python3 task-cli.py list --status done
python3 task-cli.py list --status todo
python3 task-cli.py list --status in-progress

```
> [!NOTE]
> For more details checkout ```python3 task-cli.py --help```
