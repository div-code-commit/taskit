document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');

    // Load tasks from the server
    fetch('/tasks')
        .then(response => response.json())
        .then(data => {
            data.tasks.forEach(task => addTaskToList(task));
        });

    // Add a new task
    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const due_date = document.getElementById('due_date').value;

        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, description, due_date })
        })
        .then(response => response.json())
        .then(() => {
            addTaskToList({ title, description, due_date, status: 'Pending' });
            taskForm.reset();
        });
    });

    // Function to add a task to the list
    function addTaskToList(task) {
        const li = document.createElement('li');
        li.textContent = `${task.title} - ${task.description} (Due: ${task.due_date})`;
        taskList.appendChild(li);
    }
});
