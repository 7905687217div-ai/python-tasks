# Simple To-Do List in Python

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nWhich task number do you want to remove?")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter task number: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
