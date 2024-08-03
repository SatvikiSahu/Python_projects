def task():
    tasks= []
    print("---------WELCOME TO TASK MANAGER---------")

    total_tasks = int(input("Enter the total number of tasks: "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter task {i} name: ")
        tasks.append(task_name)

    print("\nTask List:{tasks}")

    while True:
        operation=int(input("enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation==1:
            add = input("Enter new task name: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully")

        elif operation==2:
             update = input("Enter task name to update: ")
        if update in tasks:
                update_name = input("Enter new task name: ")
                ind =tasks.index(update)
                tasks[ind] = update_name
                print(f"Task '{update_name}' updated successfully")
        elif operation==3:
             delete = input("Enter task you want to delete: ")
             if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                print(f"Task '{delete}' deleted successfully")
             else:
                 print("Task not found")
        elif operation==4:
            print("\nTask List:{tasks}")
        elif operation==5:
            print("Exiting the program...")
            break
        else:
            print("Invalid operation, try again")

task()