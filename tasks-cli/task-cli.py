import argparse
import json
import os
from datetime import datetime

id_tracker = 0
__dirname = os.getcwd()
all_tasks = []
now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


if not os.path.exists(f"{__dirname}/tasks.json"):
    with open("tasks.json", "a") as f:
        f.write("[]")


with open("tasks.json", "r") as f:
    all_tasks = json.load(f)


parser = argparse.ArgumentParser(
    prog="TASK TRACKER", description="A CLI tool used to track and manage your tasks"
)
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Adding TASKS
add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("task", help="The task to be added to the tracker")

# List all TASKS
list_parser = subparsers.add_parser("list", help="List all tracked tasks")
list_parser.add_argument(
    "--status",
    choices=["todo", "in-progress", "done", "all"],
    default="all",
    help="Possible states of all tasks",
)

# Update TASKS
update_parser = subparsers.add_parser("update", help="Updates a given task")
update_parser.add_argument("id", type=int, help="Identifier of task to be updated")
update_parser.add_argument("updated_task", help="Updated task")

# Delete TASKS
delete_parser = subparsers.add_parser("delete", help="Deletes a given task")
delete_parser.add_argument("id", type=int, help="Identifier of task to be deleted")

# Mark TASKS
mark_in_progress_parser = subparsers.add_parser(
    "mark-in-progress", help="Mark a task as in progress"
)
mark_in_progress_parser.add_argument(
    "id", type=int, help="Identifier of task to be marked as in progress"
)
mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
mark_done_parser.add_argument(
    "id", type=int, help="Identifier of task to be marked as done"
)

args = parser.parse_args()

match args.command:
    case "list":
        if args.status == "todo":
            print("**** TASKS: TODO ****")
            for index, task in enumerate(all_tasks):
                if task["status"] == "todo":
                    print(f"{index}. {task['task']}")

        elif args.status == "in-progress":
            print("**** TASKS: IN-PROGRESS ****")
            for index, task in enumerate(all_tasks):
                if task["status"] == "in-progress":
                    print(f"{index}. {task['task']}")

        elif args.status == "done":
            print("**** TASKS: DONE ****")
            for index, task in enumerate(all_tasks):
                if task["status"] == "done":
                    print(f"{index}. {task['task']}")

        else:
            print("******* TASKS: ALL ********")
            for index, task in enumerate(all_tasks):
                print(f"{index}. {task['task']}")

    case "add":
        if len(all_tasks) != 0 or not all_tasks:
            id_tracker = len(all_tasks)

        with open("tasks.json", "w") as f:
            t = {
                "id": id_tracker,
                "task": args.task,
                "status": "todo",
                "created_at": now,
                "updated_at": now,
            }
            id_tracker += 1
            all_tasks.append(t)
            f.write(json.dumps(all_tasks))
            print(f"Task added successfully (ID: {t['id']})")

    case "update":
        if len(all_tasks) < 1 or args.id > len(all_tasks):
            print("[ERR] No tasks found!")
        else:
            for task in all_tasks:
                if task["id"] == args.id:
                    task["task"] = args.updated_task
                    task["updated_at"] = now
            with open("tasks.json", "w") as f:
                f.write(json.dumps(all_tasks))
                print(f"Task updated successfully (ID: {args.id})")

    case "delete":
        if len(all_tasks) < 1 or args.id > len(all_tasks):
            print("[ERR] No tasks found!")
        else:
            for index, task in enumerate(all_tasks):
                if task["id"] == args.id:
                    del all_tasks[index]
            with open("tasks.json", "w") as f:
                f.write(json.dumps(all_tasks))
                print(f"Task deleted successfully (ID: {args.id})")

    case "mark-in-progress":
        if len(all_tasks) < 1 or args.id > len(all_tasks):
            print("[ERR] No tasks found!")
        else:
            for task in all_tasks:
                if task["id"] == args.id:
                    task["status"] = "in-progress"
                    task["updated_at"] = now
            with open("tasks.json", "w") as f:
                f.write(json.dumps(all_tasks))
            print("Task marked as in-progress")

    case "mark-done":
        if len(all_tasks) < 1 or args.id > len(all_tasks):
            print("[ERR] No tasks found!")
        else:
            for task in all_tasks:
                if task["id"] == args.id:
                    task["status"] = "done"
                    task["updated_at"] = now
            with open("tasks.json", "w") as f:
                f.write(json.dumps(all_tasks))
            print("Task marked as done")
