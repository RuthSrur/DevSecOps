import json, os
from flask import jsonify

tasks_file = "tasks.json"

def ensure_file_exists():
    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w') as file:
            json.dump([], file)  # Start with an empty list of tasks


def get_all_tasks():
    with open(tasks_file, 'r') as file:
        try:
            all_tasks = json.load(file)
        except json.JSONDecodeError:
            all_tasks = []  # Return an empty list if the file is empty
    return all_tasks


def get_task(task_id):
    tasks = get_all_tasks()
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None  # Moved outside the for loop to ensure proper function logic
        
def add_task(new_task):
    tasks = get_all_tasks()
    if tasks:
        new_task["id"] = max([item['id'] for item in tasks]) + 1
    else:
        new_task["id"] = 1  # Start ID numbering from 1 if list is empty
    tasks.append(new_task)
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)
    return new_task


def delete_task(task_id):
    tasks = get_all_tasks()
    task_found = False
    for task in tasks[:]:  # Iterate a copy of the list to safely remove items
        if task['id'] == task_id:
            tasks.remove(task)
            task_found = True
    if task_found:
        with open(tasks_file, 'w') as file:
            json.dump(tasks, file, indent=4)
        return True
    return False

def update_task(task_id, updated_task):
    tasks = get_all_tasks()
    task_found = False
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            task_found = True
    if task_found:
        with open(tasks_file, 'w') as file:
            json.dump(tasks, file, indent=4)
        return True
    return False



def get_tasks_db():
    ensure_file_exists()  # Ensure file exists and is accessible
    with open(tasks_file, 'r') as file:
        try:
            all_tasks = json.load(file)
        except json.JSONDecodeError:
            all_tasks = []  # Return an empty list if the file is empty
    return all_tasks


ensure_file_exists() 



