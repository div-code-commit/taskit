from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

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

    def get_tasks(self):
        return [task.to_dict() for task in self.tasks]

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

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

task_manager = TaskManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        data = request.json
        task_manager.add_task(data['title'], data['description'], data['due_date'])
        return jsonify(success=True)
    return jsonify(tasks=task_manager.get_tasks())

@app.route('/tasks/<int:index>', methods=['PUT', 'DELETE'])
def modify_task(index):
    if request.method == 'PUT':
        data = request.json
        task_manager.update_task(index, data.get('title'), data.get('description'), data.get('due_date'), data.get('status'))
        return jsonify(success=True)
    elif request.method == 'DELETE':
        task_manager.delete_task(index)
        return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
