# ✅ Todo List API & Web App

A simple **Todo List application** built with **FastAPI** (backend API) and **Streamlit** (frontend).  
This project demonstrates how to design RESTful APIs, store data in JSON, and interact with them using a clean web UI.

---

## 🚀 Features

### 🔹 FastAPI Backend
- `GET /tasks` → Get all tasks
- `GET /task/{id}` → Get a single task by ID
- `GET /task/status/{status}` → Filter tasks by status
- `GET /tasks/search?title=keyword` → Search tasks by keyword
- `POST /add-task` → Add a new task
- `POST /task/{id}/complete` → Mark a task as completed
- `POST /task/{id}/in-progress` → Mark a task as in-progress
- `POST /task/{id}/archive` → Archive a task
- `POST /task/{id}/reopen` → Reopen a task (set back to pending)
- `DELETE /task/{id}/delete` → Delete a task

### 🔹 Streamlit Frontend
- View all tasks
- Add a new task
- Search tasks by title
- Update task status (pending, in-progress, completed, archived)
- Delete tasks

---

## 🛠️ Tech Stack
- **Python 3.13**
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **Uvicorn** (ASGI Server)
- **Pydantic** (Data validation)

---


## ⚡ Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/todo-list-api.git
cd todo-list-api
```

### 2️⃣ Create a virtual environment & install dependencies
```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows

pip install -r requirements.txt
```
### 3️⃣ Run FastAPI backend
```bash
uvicorn api:app --reload
```
### 4️⃣ Run Streamlit frontend
```bash
streamlit run frontent.py
```


