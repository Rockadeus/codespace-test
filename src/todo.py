#!/usr/bin/env python3

import argparse
import json
import os
from typing import List, Dict

TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[Dict]) -> None:
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title: str) -> None:
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {title}")

def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")

def main():
    parser = argparse.ArgumentParser(description="Simple TODO list CLI application")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    
    # List tasks command
    subparsers.add_parser("list", help="List all tasks")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()