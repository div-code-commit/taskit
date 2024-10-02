from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(title, description, due_date)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: ")) - 1
            title = input("Enter new title (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            due_date = input("Enter new due date (leave blank to skip): ")
            status = input("Enter new status (leave blank to skip): ")
            task_manager.update_task(index, title or None, description or None, due_date or None, status or None)
        elif choice == '4':
            index = int(input("Enter task index to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
