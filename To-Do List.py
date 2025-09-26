tasks=[]
def add_task(task):
    tasks.append(task)
    print(f"task'{task}' added!")
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"task'{task}' deleted!")
    else:
        print(f"task '{task}' not found!")
def display_tasks():
    print("To-Do List:")
    for task in tasks:
        print(f"   -{task}")

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Display tasks")
    print("4. Quit")
    choice = input("choose an option:")
    if choice=="1":
        task=input("enter a task:")
        add_task(task)
    elif choice=="2":
        task=input("enter a task to delete:")
        delete_task(task)
    elif choice=="3":
        display_tasks()
    elif choice=="4":
        break
    else:
        print("invalid option,try again")