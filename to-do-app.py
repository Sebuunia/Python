import time

print("Hello to my To-Do List app!")

tasks = []

def add_tasks():
    task = input("Enter a task: ")
    tasks.append(task)

def view_tasks():
    print(tasks)

def del_tasks():
    task = input("Enter the task you want to delete: ")
    if task in tasks:
        time.sleep(1)
        print(f"Task {task} deleted.")
        tasks.remove(task)
    else:
        print("Task not found.")

def exit():
    print("Goodbye!")
    quit()

while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        del_tasks()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice.")
