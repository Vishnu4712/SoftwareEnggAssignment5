tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def remove_task(task_number):
    if not tasks:
        print("No tasks to remove.")
        return

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task \"{removed_task}\" removed.')
    else:
        print("Invalid task number. Please enter a valid number.")

if __name__ == "__main__":
    add_task("Finish Assignment")
    add_task("Submit Report")
    list_tasks()

    print("\nTrying to remove Task 1...")
    remove_task(1)
    list_tasks()

    print("\nTrying to remove an invalid task...")
    remove_task(5)  # This will now show a proper error message.
