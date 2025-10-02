import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # FastAPI runs locally

st.set_page_config(page_title="Todo List", layout="centered")

st.title("✅ Todo List (FastAPI + Streamlit)")

# ---- Sidebar navigation ----
menu = ["View Tasks", "Add Task", "Search Task", "Update Status", "Delete Task"]
choice = st.sidebar.radio("Navigation", menu)


# ---- View all tasks ----
if choice == "View Tasks":
    st.subheader("All Tasks")
    response = requests.get(f"{BASE_URL}/tasks")
    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            for t in tasks:
                st.write(f"**ID**: {t['id']} | **Title**: {t['title']} | **Status**: {t['status']}")
                st.caption(t.get("description", ""))
        else:
            st.info("No tasks found.")
    else:
        st.error("Failed to fetch tasks.")


# ---- Add Task ----
elif choice == "Add Task":
    st.subheader("Add a New Task")
    with st.form("add_task_form"):
        task_id = st.text_input("Task ID")
        title = st.text_input("Task Title")
        description = st.text_area("Description")
        status = st.selectbox("Status", ["pending", "in-progress", "completed"])
        submit = st.form_submit_button("Add Task")

    if submit:
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "status": status
        }
        res = requests.post(f"{BASE_URL}/add-task", json=new_task)
        if res.status_code == 200:
            st.success("Task added successfully!")
        else:
            st.error(res.json().get("detail", "Error adding task"))


# ---- Search Task ----
elif choice == "Search Task":
    st.subheader("Search Task by Title")
    keyword = st.text_input("Enter keyword")
    if st.button("Search"):
        res = requests.get(f"{BASE_URL}/taks/search", params={"title": keyword})
        if res.status_code == 200:
            tasks = res.json()
            for t in tasks:
                st.write(f"**ID**: {t['id']} | **Title**: {t['title']} | **Status**: {t['status']}")
        else:
            st.warning("No task found.")


# ---- Update Status ----
elif choice == "Update Status":
    st.subheader("Update Task Status")
    task_id = st.text_input("Enter Task ID")
    new_status = st.selectbox("Choose new status", ["pending", "in-progress", "completed", "archived"])
    if st.button("Update"):
        if new_status == "pending":
            res = requests.post(f"{BASE_URL}/task/{task_id}/reopen")
        elif new_status == "in-progress":
            res = requests.post(f"{BASE_URL}/task/{task_id}/in-progess")
        elif new_status == "completed":
            res = requests.post(f"{BASE_URL}/task/{task_id}/complete")
        elif new_status == "archived":
            res = requests.post(f"{BASE_URL}/task/{task_id}/archive")

        if res.status_code == 200:
            st.success(res.json()["message"])
        else:
            st.error(res.json().get("detail", "Error updating task"))


# ---- Delete Task ----
elif choice == "Delete Task":
    st.subheader("Delete a Task")
    task_id = st.text_input("Enter Task ID to delete")
    if st.button("Delete"):
        res = requests.delete(f"{BASE_URL}/task/{task_id}/delete")
        if res.status_code == 200:
            st.success(res.json()["message"])
        else:
            st.error(res.json().get("detail", "Error deleting task"))
