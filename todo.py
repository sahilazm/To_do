# Import the required modules
import os

# Define a function to display the menu
def display_menu():
    print("To-Do List App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

# Define a function to add a task
def add_task():
    task = input("Enter a task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Define a function to remove a task
def remove_task():
    task_number = int(input("Enter the task number to remove: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if task_number <= len(tasks):
        del tasks[task_number - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number!")

# Define a function to view tasks
def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()