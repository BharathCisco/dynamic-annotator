# Task Management CLI

## Overview
Task Management CLI is a simple command-line application for managing tasks. Users can add, remove, and list tasks, which are stored in a JSON file (`tasks.json`). The application leverages the `tabulate` library for displaying tasks in a formatted table.

## Features
- **Add Task**: Users can add new tasks with a name, due date, and category.
- **Flush Task**: Allows users to remove tasks by their ID.
- **Flush All**: Deletes all tasks from the task list.
- **List Tasks**: Displays all tasks in a neatly formatted table, sorted by due date (in descending order).
- **Persistent Storage**: Tasks are saved in `tasks.json`, ensuring data is preserved between runs.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.6 or later).

### Install Dependencies
```sh
pip install tabulate
```

## Usage
Run the CLI tool using the following command:
```sh
python -m task_management
```

### Available Commands
| Command | Description |
|---------|-------------|
| `1` | Add a new task |
| `2` | Remove a task by ID |
| `3` | Flush all tasks |
| `4` | Exit the program |

## Example
```sh
Choose an option:
1. Add Task
2. Remove Task
3. Flush All
4. Exit
Choose an option: 1
Enter task name: Buy Groceries
Enter due date (YYYY-MM-DD): 2025-03-06
Enter category: Shopping
Task added successfully! Task ID: 4d95a740-8e38-4a77-b23a-7b162d8b9f6a
```
