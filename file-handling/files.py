import os

# File Setup

DATA_FOLDER = "data"
TASK_FILE = os.path.join(DATA_FOLDER, "tasks.txt")

os.makedirs(DATA_FOLDER, exist_ok=True)



def add_tasks():
    # Add tasks to the text file.

    try:
        total = int(input("How many tasks do you want to add? : "))

        with open(TASK_FILE, "a") as file:
            for i in range(total):
                task = input(f"Task {i + 1}: ").strip()

                if task:
                    file.write(task + "\n")

        print("\n Tasks added successfully!")

    except ValueError:
        print(" Please enter a valid number.")


def view_tasks():
    # Display all saved tasks.

    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("\n No tasks found.")
            return

        print("\n========== YOUR TASKS ==========")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

        print("===============================\n")

    except FileNotFoundError:
        print("Task file not found.")


def menu():

    while True:

        print("\n====== SIMPLE TASK MANAGER ======")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_tasks()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\n Session Ended.")
            break

        else:
            print("Invalid option.")



if __name__ == "__main__":
    try:
        menu()

    except KeyboardInterrupt:
        print("\nProgram Interrupted.")

    except Exception as e:
        print("Unexpected Error:", e)
