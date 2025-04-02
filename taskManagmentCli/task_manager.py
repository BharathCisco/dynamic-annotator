from beartype import beartype

import json
import uuid
from json.decoder import JSONDecodeError
from datetime import datetime

@beartype
def add_number(a: int, b: int) -> int:
    return a + b

print(add_number(1, 2))  # ✅ Works fine
print(add_number("1", 2))  # ✅ Works fine

class TaskManager:
    @beartype
    def __init__(self, db_file='tasks.json'):
        self.db_file = db_file
        self.tasks = self.load_tasks()

    # Add a new task
    @beartype
    def add_task(self, task_name, due_date, category):
        while not self.validate_date(due_date):
            due_date = input("Enter due date (YYYY-MM-DD): ")

        new_id = str(uuid.uuid4())  # Generate a unique ID
        new_task = {"id": new_id, "task": task_name, "due_date": due_date, "category": category}
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully! Task ID: {new_id}")

    # Remove a task by ID
    @beartype
    def remove_task(self, task_id):
        task = next((task for task in self.tasks if task["id"] == task_id), None)
        if task:
            self.tasks = [task for task in self.tasks if task["id"] != task_id]
            self.save_tasks()
            print("Task removed successfully!")
        else:
            print("Task ID not found!")

    # Load tasks from the JSON file
    @beartype
    def load_tasks(self):
        try:
            with open(self.db_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            return []

    # Save tasks to the JSON file
    @beartype
    def save_tasks(self):
        with open(self.db_file, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Validate date format (YYYY-MM-DD)
    @beartype
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # List tasks, sorted by due date in descending order
    @beartype
    def list_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x['due_date'], reverse=True)
        return sorted_tasks

    @beartype
    def flush_tasks(self):
        self.tasks = []  # Empty the task list
        self.save_tasks()
        print("All tasks have been deleted.")
