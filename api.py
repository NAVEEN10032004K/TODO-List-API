from fastapi import FastAPI, HTTPException, Path, Query
from validation_model import UserInput
import json
import os

app = FastAPI()

def load():
    path = 'list.json'
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return []

def save(data):
    with open("list.json", 'w') as f:
        json.dump(data, f, indent=4)



@app.get("/")
def home():
    return {"message": "TODO List API is running."}

@app.get("/tasks")
def get_all_tasks():
    return load()

@app.get("/task/{task_id}")
def get_task(task_id: str = Path(..., description="Task ID", example="1")):
    data = load()
    for task in data:
        if task["id"] == task_id:   # Match with id in JSON
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

@app.get('/task/status/{status}')
def get_task_by_status(status: str):
    data = load()
    filtered = [task for task in data if task['status'] == status]

    if not filtered:
        raise HTTPException(status_code=404, detail=f"Taks not found with status: {status}")
    
    return filtered

@app.get('/taks/search')
def search_task(title: str = Query(..., description="Keyword to search in task title", example="title")):
    data = load()
    result = [task for task in data if title.lower() in task['title'].lower()]

    if not result:
        raise HTTPException(status_code=404, detail=f"Task {title} Not Found.")
    return result

@app.post('/add-task')
def add_task(task: UserInput):
    data = load()
    for existing_task in data:
        
        if existing_task["id"] == task.id:
            raise HTTPException(status_code=400, detail=f"Task id: {task.id} already exist.")
        
    data.append(task.model_dump())
    save(data)
    return HTTPException(status_code=200, detail=f"Task with id: {task.id} added successfully.")

@app.post('/task/{id}/reopen')
def task_reopen(id: str):
    data = load()  # list of tasks
    for task in data:
        if task['id'] == id:
            task['status'] = "pending"
            save(data)  # save full list back
            return {"message": f"Task {id} marked as pending."}

    # if loop finishes without finding task
    raise HTTPException(status_code=404, detail=f"Task with ID {id} does not exist.")

@app.post('/task/{id}/complete')
def task_completed(id: str):
    data = load()  # list of tasks
    for task in data:
        if task['id'] == id:
            task['status'] = "completed"
            save(data)  # save full list back
            return {"message": f"Task {id} marked as completed."}

    # if loop finishes without finding task
    raise HTTPException(status_code=404, detail=f"Task with ID {id} does not exist.")

@app.post('/task/{id}/in-progess')
def task_in_progess(id: str):
    data = load()  # list of tasks
    for task in data:
        if task['id'] == id:
            task['status'] = "in-progress"
            save(data)  # save full list back
            return {"message": f"Task {id} marked as completed."}

    # if loop finishes without finding task
    raise HTTPException(status_code=404, detail=f"Task with ID {id} does not exist.")


@app.post('/task/{id}/archive')
def archive_task(id: str):
    data = load()  # list of tasks
    for task in data:
        if task['id'] == id:
            task['status'] = "archived"
            save(data)  # save full list back
            return {"message": f"Task {id} marked as archived."}

    # if loop finishes without finding task
    raise HTTPException(status_code=404, detail=f"Task with ID {id} does not exist.")

@app.delete('/task/{id}/delete')
def delete_task(id: str):
    data = load()
    updated_task_list = [task for task in data if task['id'] != id]
    if len(updated_task_list) == len(data):
        raise HTTPException(status_code=404, detail=f"Task with ID {id} does not exist.")    

    save(updated_task_list)        
    return {"message": "Task with ID {id} deleted."}