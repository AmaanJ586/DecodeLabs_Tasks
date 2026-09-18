import json, os

DB_file = "to_do_tasks.json"
all_tasks = []

def load_tasks():
    global all_tasks
    if os.path.exists(DB_file):
        try:
            with open(DB_file, "r") as f:
                all_tasks = json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Error Loading tasks. Starting with new empty list.")
    else:
        all_tasks = []

def save_tasks():
    with open("to_do_tasks.json", "w") as f:
        json.dump(all_tasks, f, indent = 2)

def add_tasks(detail):
    new_id = (max((t["id"] for t in all_tasks), default = 0)) + 1
    task = { "id" : new_id, "Task" : detail, "Status" : False}
    all_tasks.append(task)
    save_tasks()
    print("Task added successfully...")

def view_tasks():
    if not all_tasks:
        print("No tasks found...")
        return
    for index, task in enumerate(all_tasks, start = 1):
        status = "Done" if task["Status"] else "Pending"
        print(f"{index}. {status} | {task['id']} | {task['Task']}")

def task_marker(task_id):
    for task in all_tasks:
        if task['id'] == task_id:
            task['Status'] = True
            save_tasks()
            return

    print("Task not found...")


def delete_task(task_id):
    global all_tasks
    pre_len = len(all_tasks)
    all_tasks = [task for task in all_tasks if task['id'] != task_id]
    if len(all_tasks) < pre_len:
        save_tasks()
        print("Task was successfully deleted...")
    else:
        print("No such task found...")

def print_menu():
    print("""
        To-Do List Application
        1. Add Task
        2. View Tasks
        3. Mark Task as Done
        4. Delete Task
        5. Exit
    """)

def main():
    load_tasks()
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter task description: ")
            if description:
                add_tasks(description)
            else:
                print("Description can't be empty...")
        elif choice == 2:
            view_tasks()

        elif choice == 3:
            view_tasks()
            try:
                task_id = int(input("Enter the ID of the task to update: "))
                task_marker(task_id)
            except ValueError:
                print("Enter a valid number...")

        elif choice == 4:
            view_tasks()
            try:
                task_id = int(input("Enter the ID of the task to update: "))
                delete_task(task_id)
            except ValueError:
                print("Enter a valid number...")

        elif choice == 5:
            print("Exiting the application")
            break
        else:
            print("Invalid choice. Please try again...")

if __name__ == "__main__":
    main()