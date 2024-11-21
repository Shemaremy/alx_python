import json

def export_all_tasks_to_json(users):
    data = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]
        tasks = user["tasks"]
        if tasks:  # Only record if there are tasks for the user
            data[user_id] = {"username": username, "tasks": [{"title": task["title"], "completed": task["completed"]} for task in tasks]}
        else:
            data[user_id] = {"username": username, "tasks": []}

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Example data for multiple users
users = [
    {"id": "1", "username": "user1", "tasks": [{"title": "Task 1", "completed": True}, {"title": "Task 2", "completed": False}]},
    {"id": "2", "username": "user2", "tasks": [{"title": "Task 3", "completed": True}, {"title": "Task 4", "completed": True}]},
    {"id": "3", "username": "user3", "tasks": []},  # No tasks for this user
]

export_all_tasks_to_json(users)