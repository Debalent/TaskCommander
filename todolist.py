#!/usr/bin/env python3
import argparse
import os
import json
import sys

# File used to persist tasks
DATA_FILE = 'tasks.json'

def load_tasks():
    """
    Load tasks from the JSON file. If the file does not exist,
    create it with an empty list. Tasks are stored as dictionaries:
    {"description": <str>, "completed": <bool>}.
    """
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump([], f)
        except Exception as e:
            print(f"Error creating {DATA_FILE}: {e}")
            sys.exit(1)
    try:
        with open(DATA_FILE, 'r') as f:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                raise ValueError("Tasks file is corrupted!")
            return tasks
    except Exception as e:
        print(f"Error loading tasks: {e}")
        sys.exit(1)

def save_tasks(tasks):
    """Save the list of tasks back to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")
        sys.exit(1)

def add_task(description):
    """Add a new task with the specified description."""
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """List all stored tasks with their status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task.get("completed") else "✗"
        print(f"{idx}. [{status}] {task.get('description')}")

def remove_task(index):
    """
    Remove a task using its 1-based index.
    Exits the program if an invalid index is provided.
    """
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        sys.exit(1)
    removed_task = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Task removed: {removed_task.get('description')}")

def complete_task(index):
    """
    Mark a task as completed using its 1-based index.
    Checks if the task is already completed.
    """
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        sys.exit(1)
    task = tasks[index - 1]
    if task.get("completed"):
        print("Task is already completed.")
    else:
        task["completed"] = True
        save_tasks(tasks)
        print(f"Task marked as completed: {task.get('description')}")

def main():
    parser = argparse.ArgumentParser(
        description="TaskCommander CLI: Manage your tasks with a robust command-line to-do list."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Sub-command: add
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="The task description (use quotes)")

    # Sub-command: list
    subparsers.add_parser("list", help="List all tasks")

    # Sub-command: remove
    parser_remove = subparsers.add_parser("remove", help="Remove a task by its number")
    parser_remove.add_argument("number", type=int, help="Task number to remove (1-based)")

    # Sub-command: complete
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("number", type=int, help="Task number to complete (1-based)")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "remove":
        remove_task(args.number)
    elif args.command == "complete":
        complete_task(args.number)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
