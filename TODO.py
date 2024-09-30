class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False

    def change_name(self, new_name):
        self.name = new_name

    def change_due_date(self, new_date):
        self.due_date = new_date

    def complete(self):
        self.completed = True
    # Initialize the tasks list
tasks = []

# Building the Menu
menu = {
    1: 'Add New Task',
    2: 'View All Tasks',
    3: 'Mark Task as Completed',
    4: 'Delete Task',
    5: 'Save Tasks',
    6: 'Load Tasks',
    7: 'Quit'
}
# Printing the Menu options
print('To-Do List Menu')
for key, value in menu.items():
    print(f'{key} -- {value}')

choice = input('Please enter your selection: ')
# Implementing the Functions and adding a new task
def add_task():
    name = input('Enter task name: ')
    due_date = input('Enter due date: ')
    new_task = Task(name, due_date)
    tasks.append(new_task)

# Viewing all tasks
def view_tasks():
    print('All Tasks:')

    for task in tasks:
        print(f'Name: {task.name}')
        print(f'Due Date: {task.due_date}')
        print(f'Completed: {task.completed}')
        print()
    # Marking Tasks as completed
def complete_task():
    index = int(input('Enter the task number to mark as completed: '))
    tasks[index - 1].complete()
    # Deleting Tasks
def delete_task():
    index = int(input('Enter the task number to delete: '))
    tasks.pop(index - 1)

    # Save Tasks
import pickle

def save_tasks():
    file = open('tasks.dat', 'wb')

    pickle.dump(tasks, file)

    file.close()

    # Loading Tasks
def load_tasks():
    global tasks

    file = open('tasks.dat', 'rb')
    tasks = pickle.load(file)

    file.close()

    # Main Application Loop

def display_menu():
    print('To-Do List Menu')
    for key, value in menu.items():
        print(f'{key} -- {value}')

while choice != '7':

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()


    input('Press enter to return to menu: ')
    display_menu()
    choice = input('Please enter your selection: ')