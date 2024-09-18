# SEBASTIAN MAIN -- FINAL PROJECT

def new_tasks(tasks):
    new_task = input("What is your new task (ID,description,project,due date): ")
    tokens = new_task.strip().split(",")
    ID = int(tokens[0])
    description = tokens[1]
    project = tokens[2]
    date = tokens[3]
    new_task = [ID, description, project, date]
    tasks.append(new_task)

def save_tasks(tasks):
    f2 = open("new_tasks.txt", "w")
    print("Saving your tasks...")
    for task in tasks:
        f2.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]} \n")
    f2.close()
    print("\nGoodbye!")


def get_tasks():
    f = open("tasks.txt", "r")
    tasks = []
    for line in f:
        tokens = line.strip().split(",")
        ID = int(tokens[0])
        description = tokens[1]
        project = tokens[2]
        date = tokens[3]
        
        task = [ID, description, project, date]
        tasks.append(task)
    
    f.close()
    return tasks
    
def main():
    tasks = get_tasks()
    print("\033[1mHere are the operations:\033[0m \n [1] View all tasks \n [2] View all tasks by date \n [3] View tasks by project \n [4] Add a task \n [5] Save tasks and quit")
    while True:
        operation = int(input("\n\033[1mWhat operation would you like to do: \033[0m"))
        if operation == 1:
            for task in tasks:
                print(f"\nTask: {task[0]}, {task[1]}, {task[2]}, {task[3]}")
            
        if operation == 2:
            date_tasks = str(input("\n\033[1mWhat date would you like to see (mm/dd/yyyy): \033[0m"))
            for task in tasks:
                if date_tasks == task[3]:
                    print(f"\nTask: {task[0]}, {task[1]}, {task[2]}, {task[3]}")
                    
        if operation == 3:
            project_tasks = str(input("\n\033[1mWhat project would you like to see: \033[0m"))
            for task in tasks:
                if project_tasks == task[2]:
                    print(f"\nTask: {task[0]}, {task[1]}, {task[2]}, {task[3]}")
                    
        if operation == 4:
            new_tasks(tasks)
            
        if operation == 5:
            save_tasks(tasks)
            break
                    
        if operation == 0 or operation > 5:
            print("Invalid input. Please try again")

main()