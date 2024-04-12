import json, os
from flask import jsonify

tasks_file = "/home/ruth/DevSecOps/tasksapp/tasks.json"

# def ensure_file_exists():
#     if not os.path.exists(tasks_file):
#      with open(tasks_file, 'w') as file:
#         initial_data = {"id":1, "tasks":[]}
#         json.dump(initial_data, file)
# ensure_file_exists()

def get_all_tasks():
    with open(tasks_file, 'r') as file:
        all_tasks = json.load(file)
    return all_tasks

def get_task(task_id):
    tasks = get_all_tasks()
    for task in tasks:
        if task['id'] == task_id:
            return task
        else:
             return None
        
def add_task(new_task):
    tasks = get_all_tasks()
    new_task["id"] = max([item['id'] for item in tasks]) + 1
    tasks.append(new_task)
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)
    return new_task


def delete_task(task_id):
    tasks= get_all_tasks()
    for task in tasks[:]:
        if task['id'] == task_id:
            tasks.remove(task)
            with open(tasks_file,'w') as file:
                json.dump(tasks, file)
            return (task)  
        

def update_task(task_id,updated_task):
    tasks= get_all_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            with open(tasks_file, 'w') as file:
                json.dump(tasks, file)
            return updated_task 
        

def get_tasks_db():
    try:
        dbfile = open(tasks_file)
    except FileNotFoundError:
        dbfile = open('tasks.json', mode = 'w', encoding='utf-8')
        initial_data = {"id":1, "tasks":[]}
        json.dump(initial_data, dbfile)
    return dbfile  






