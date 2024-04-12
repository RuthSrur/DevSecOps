from flask import Flask,request,jsonify
import tasks_db as tasks_db
import json

app = Flask(__name__)

@app.route("/tasks")
def get_all_tasks():
    all_tasks = tasks_db.get_all_tasks()
    return all_tasks

@app.route("/tasks/<int:task_id>", methods=['GET'])
def get_task(task_id):
    task = tasks_db.get_task(task_id)
    if task != None:
        return task
    else:
        return ('Task not found')


@app.route("/tasks", methods=['POST'])
def add_task():
    new_task = request.json
    tasks_db.add_task(new_task)
    return new_task

@app.route("/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    deleted_task = tasks_db.delete_task(task_id)
    if deleted_task:
        return ("Task deleted successfully")
    else:
        return ("Task not found") 
    
@app.route("/tasks/<int:task_id>", methods=['PUT'])
def update_task(task_id):
    task_data= request.json
    updated_task = tasks_db.update_task(task_id,task_data)
    if updated_task:
        return ("Task updated successfully")
    else:
        return ("task not found")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)