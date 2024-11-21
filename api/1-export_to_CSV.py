import csv

def export_tasks_to_csv(user_id, username, tasks):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([user_id, username, task["completed"], task["title"]])

# Example data
user_id = "123"
username = "example_user"
tasks = [
    {"title": "Task 1", "completed": True},
    {"title": "Task 2", "completed": False},
    {"title": "Task 3", "completed": True}
]

export_tasks_to_csv(user_id, username, tasks)