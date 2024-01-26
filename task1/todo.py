import os

def display_menu():
    print("To-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. To view Completed Task")
    print("5. Exit")

def view_tasks():
    file_path = os.path.join(os.path.dirname('todo.py'), "tasks.txt")
    try:
        with open(file_path, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_completed():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    file_path1 = os.path.join(os.path.dirname('todo.py'), "completed_file.txt")

    try:

        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
                print("No tasks found.")

        if 0 <= task_number < len(tasks):
            completed_task = tasks.pop(task_number)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            with open(file_path1, "a") as completed_file:
                    completed_file.write(completed_task)

            print(f"Task '{completed_task.strip()}' marked as completed.")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print(f"Error: {file_path1} not found.")

def view_completed_task():
    file_path2 = os.path.join(os.path.dirname('todo.py'), "completed_file.txt")
    try:
        with open(file_path2, "r") as file:
            completed_tasks = file.readlines()
            if not completed_tasks:
                print("No tasks found.")
            else:
                print("Completed Tasks:")
                for idx, task in enumerate(completed_tasks, start=1):
                    print(f"{idx}. {task.strip()}")
            
    except FileNotFoundError:
        print(f"Error: {file_path2} not found.")

        
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            view_completed_task()
        elif choice == "5":
            print("Exiting the application. THANKYOU!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
