tasks = []

def addTask():
    global tasks
    task = input('Enter your task: ')
    tasks.append(task)
    saveTasks()
    print(f"Task '{task}' added!")

def viewTasks():
    global tasks
    if not tasks:
        print('There are no tasks!')
    else:
        print('Your tasks: ')
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')

def deleteTask():
    global tasks
    task = input('Enter a task to delete: ')
    if task in tasks:
        tasks.remove(task)
        saveTasks()
        print(f"Task '{task}' deleted!")
    else:
        print(f"Task '{task}' not found!")

def loadTasks():
    global tasks
    try:
        with open('tasks.txt', 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        print(tasks)
    except FileNotFoundError:
        tasks = []

def saveTasks():
    with open('tasks.txt', 'w') as file:
        file.writelines(task + '\n' for task in tasks)

if __name__ == '__main__':
    print('Welcome to the to do list app :)')
    loadTasks()

    while True:
        print("\n")
        print('Please choose your task: ')
        print('1. Add Task: ')
        print('2. View Tasks: ')
        print('3. Delete Task: ')
        print('4. Quit')

        choice = int(input('Enter your # of choice: '))

        if choice == 1:
            addTask()
        elif choice == 2:
            viewTasks()
        elif choice == 3:
            deleteTask()
        elif choice == 4:
            break
        else:
            print('Invalid choice. Please try again.')

    print('Thank you for your task!')
