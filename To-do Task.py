import os

your_task = []

list_task = ['1','2','3','4','5',]

def indent():
    print("-"* 50)
    
def quit():
    os.system("cls")
    print("Goodbye!")

def delete_task():
    os.system("cls")
    for i, task in enumerate(your_task, start=1):
        print(f"{i}. {task}")
    delete_num = int(input("Enter the task number to delete: "))
    if delete_num >= 1 and delete_num <= len(your_task):
        your_task.pop(delete_num - 1)
def mark_task_comp():
    os.system("cls")
    print("To-Do List:")
    for i, task in enumerate(your_task, start=1):
        print(f"{i}. {task}")
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if task_number < len(your_task):
        your_task[task_number] = your_task[task_number] + " [x]"
        print("Task marked as completed!")
def add_task():
    os.system("cls")
    added = input("Enter the description: ")
    your_task.append(added)
    os.system("cls")
    
def list_tasks():
    os.system("cls")
    print("Task:\n")
    for i, task in enumerate(your_task, start=1):
        print(f"{i}: {task}")
    indent()

while True:
    print("Welcome to the To-Do List Manager!")
    print("1. Add Task \n2. To-Do List \n3. Mark Task as completed \n4. Delete Task \n5. Quit")
    choice = input("Enter your choice(1/2/3/4/5): ")
    if choice == "1":
        indent()
        add_task()
    elif choice == "2":
        indent()
        list_tasks()
    elif choice == "3":
        indent()
        mark_task_comp()
    elif choice == "4":
        indent()
        delete_task()
    elif choice == "5":
        indent()
        quit()
        raise
    else:
        print("Error")
        os.system("cls")