""" This is a simple command-line task manager application that allows users to add, remove, view, save, and load tasks. The tasks are stored
    in a text file, and the application provides a user-friendly interface for managing them. """


import os

# ========= Folder & File Setup ========= #

DATA_FOLDER = "data"
TASK_FILE = os.path.join(DATA_FOLDER, "tasks.txt")
SAVED_FILE = os.path.join(DATA_FOLDER, "saved_tasks.txt")

os.makedirs(DATA_FOLDER, exist_ok=True)

# auto create file
open(TASK_FILE, "a").close()

# ========== File Handling Class ========== #
class FileHandling:
    def add_task(self):
        try:
            # ask user for the number of tasks to add
            number_of_tasks = int(input("Enter number of task(s) to add: "))
            # open a file and write data in it
            with open("data/tasks.txt","a") as f:
                for i in range(number_of_tasks):
                    f.write(input(f"Task {i+1}: ") + "\n")
        except FileNotFoundError:
            print("Create a File First.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print("Unexpected Error: ",e)


    def remove_task(self):
        try:
            # open the file and store the data in list
            with open("data/tasks.txt","r") as f:
                data = f.readlines()
                for i,task in enumerate(data,1):
                    print(f"{i}. {task.strip()}")
                # get the index of task to remove
                while True:
                     index = int(input("Enter the index of task to remove: "))
                     if index <= 0 or index > len(data):
                        print("Index Invalid!")
                        continue
                     break
                # remove the task from list
                data.pop(index - 1)
                # write the updated list back to the file
                with open("data/tasks.txt","w") as f:     
                    f.writelines(data)
        except FileNotFoundError:
            print("Create a File First.")
        except Exception as e:
            print("Unexpected Error: ",e)   

    def view_tasks(self):
        try:
            # try to open the file and read tasks
            with open("data/tasks.txt","r") as f:
                data = f.readlines()
                if not data:
                    print("No data found in the file.")
                else:
                    for i,task in enumerate(data,1):
                        print(f"{i}. {task.strip()}")
        except FileNotFoundError:
            print("Create a File First.")
        except Exception as e:
            print("Unexpected Error: ",e)

    def save_tasks(self):
        try:
            # look for the tasks(if exists) in tasks.txt
            with open("data/tasks.txt","r") as f:
                data = f.readlines()
                if not data:
                    print("No data found in the file.")
                else:
                    # if data is in tasks.txt then create a new file and save those tasks 
                    with open("data/saved_tasks.txt","w") as f2:
                        f2.writelines(data)
                    print("Task(s) saved successfully.")
        except FileNotFoundError:
            print("Create a File First.")
        except Exception as e:
            print("Unexpected Error: ",e)

    def load_tasks(self):
        try:
            # open the saved_tasks.txt and print the data
            with open("data/saved_tasks.txt","r") as f:
                data = f.readlines()
                if not data:
                    print("No data found in the file.\nTry creating a file and add your tasks there first!")
                else:
                    for i,task in enumerate(data,1):
                        print(f"{i}. {task.strip()}")
        except FileNotFoundError:
            print("Create a File First.")
        except Exception as e:
            print("Unexpected Error: ",e)


def intro(title="Python Task Manager"):
    print("=" * 50)
    print(title)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")
    print("=" * 50)


def main():
    intro(title="Welcome to Python Task Manager")
    while True:
        try: 
            choice = int(input("Enter your choice:"))
            if choice == 1:
                FileHandling().add_task()
                print("-" * 50)
            elif choice == 2:
                FileHandling().remove_task()
                print("Task(s) removed successfully.")
                print("-" * 50)
            elif choice == 3:
                FileHandling().view_tasks()
                print("-" * 50)
            elif choice == 4:
                FileHandling().save_tasks()
                print("-" * 50)
            elif choice == 5:
                FileHandling().load_tasks()
                print("-" * 50)
            elif choice == 6:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
                print("-" * 50)

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print("Unexpected Error: ",e)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Unexpected Error: ",e)      
