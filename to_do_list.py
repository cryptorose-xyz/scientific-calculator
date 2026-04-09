#To do list APP

tasks = []  # Initialize an empty list to store tasks

def add_task(new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added to the list.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task_item in enumerate(tasks, start=1):
            print(f"{index}. {task_item}")
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task number.")
# --- MAIN PROGRAM ---
print("Welcome to Roseline's To-Do List App 📝✨")
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        try:
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
