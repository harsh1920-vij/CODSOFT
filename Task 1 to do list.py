import json
import os

# File to store tasks
TODO_FILE = "todo_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. [{status}] {task['title']}")
    print()

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter the task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("Task added.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as done: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"Task '{removed['title']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting To-Do List App. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-5.")

if __name__ == "__main__":
    main()
