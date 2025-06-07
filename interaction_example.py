#!/usr/bin/env python3
"""
interaction_example.py

This script demonstrates how to interact with the TaskCommander CLI by importing its functions.
It adds tasks, lists them, marks a task as complete, and then removes a task.
"""

import os
import json
import todolist  # This assumes that todolist.py is in the same directory or in your PYTHONPATH

# For demonstration – reset the tasks file for a clean test environment.
def reset_tasks_file():
    tasks_file = 'tasks.json'
    if os.path.exists(tasks_file):
        os.remove(tasks_file)
    # Create a new empty tasks file.
    with open(tasks_file, 'w') as f:
        json.dump([], f)

def demo_interaction():
    # Start fresh for demo purposes.
    reset_tasks_file()
    print("=== Clean Tasks File Created ===\n")
    
    # Add some tasks.
    print("Adding tasks...")
    todolist.add_task("Buy groceries")
    todolist.add_task("Prepare report")
    
    # List tasks after addition.
    print("\nListing tasks after adding:")
    todolist.list_tasks()
    
    # Mark the first task as complete.
    print("\nMarking the first task as complete...")
    todolist.complete_task(1)
    
    # List tasks after completing one.
    print("\nListing tasks after marking complete:")
    todolist.list_tasks()
    
    # Remove the completed task.
    print("\nRemoving the completed task...")
    todolist.remove_task(1)
    
    # Final listing.
    print("\nFinal list of tasks:")
    todolist.list_tasks()

if __name__ == '__main__':
    demo_interaction()
