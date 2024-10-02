import json

class Task:
    def __init__(self, title, description, due_date, status='Pending'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status
        }

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date):
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f'Task "{title}" added successfully.')

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Status: {task.status}")

    def update_task(self, index, title=None, description=None, due_date=None, status=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if status:
                task.status = status
            self.save_tasks()
            print(f'Task "{task.title}" updated successfully.')
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f'Task "{removed_task.title}" deleted successfully.')
        else:
            print("Invalid task index.")
