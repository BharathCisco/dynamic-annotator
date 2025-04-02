import sys
from tabulate import tabulate
from task_manager import TaskManager
from beartype import beartype

@beartype
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(1, 2))  # ✅ Works fine
print(add_numbers("1", 2))  # ✅ Works fine


@beartype
def main():
    task_manager = TaskManager()

    while True:
        tasks = task_manager.list_tasks()
        display_tasks(tasks)

        print("\n1. Add Task")
        print("2. Flush Task")
        print("3. Flush All")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            while not task_manager.validate_date(due_date):
                due_date = input("Enter due date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            task_manager.add_task(task_name, due_date, category)
        elif choice == '2':
            try:
                task_id = int(input("Enter task id to flush: "))
                task_manager.remove_task(task_id)
            except ValueError:
                print("Invalid task ID entered.")
        elif choice == '3':
            confirm = input("Are you sure you want to delete all tasks? (y/n): ")
            if confirm.lower() == "y":
                task_manager.flush_tasks()
        elif choice == '4':
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

@beartype
def display_tasks(tasks):
    headers = ["ID", "Task", "Due Date", "Category"]
    task_data = [(task['id'], task['task'], task['due_date'], task['category']) for task in tasks]
    table = tabulate(task_data, headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
