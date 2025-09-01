tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\nOptions: add, show, remove, quit")
    command = input("Enter command: ").lower()

    if command == "quit":
        break
    elif command == "add":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")
    elif command == "show":
        show_tasks()
    elif command == "remove":
        try:
            index = int(input("Enter task number to remove: "))
            tasks.pop(index - 1)
            print("Task removed.")
        except (ValueError, IndexError):
            print("Invalid task number.")
    else:
        print("Unknown command.")