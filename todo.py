# To-Do List App
# Week 2 Mini Project

FILENAME = "tasks.txt"


def load_tasks():
    """Load saved tasks from file."""
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            
            for line in lines:
                clean_line = line.strip()
                tasks.append(clean_line)
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save current tasks to file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📌 No tasks yet!")
        return

    print("\n📝 Your To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    """Add a new task."""
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("✔ Task added")


def remove_task(tasks):
    """Remove a task by number."""
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"🗑 Removed: {removed}")
    except (ValueError, IndexError):
        print("❌ Invalid selection.")


def main():
    tasks = load_tasks()
    print("=== 🗒️ Simple To-Do List App ===")

    while True:
        print("\nChoose an option:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Changes saved. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
