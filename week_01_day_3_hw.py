tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks

def uncompleted(list_of_tasks):
    uncompleted_tasks = []
    
    for task in list_of_tasks:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
        
    print(uncompleted_tasks)

uncompleted(tasks)



# 2. Print a list of completed tasks

def completed(list_of_tasks):
    completed_tasks = []
    
    for task in list_of_tasks:
        if task["completed"] == True:
            completed_tasks.append(task)
        
    print(completed_tasks)

completed(tasks)



# 3. Print a list of all task descriptions

def descriptions(list_of_tasks):
    list_of_descriptions = []
    
    for task in list_of_tasks:
        desc = list_of_tasks[list_of_tasks.index(task)]["description"]
        list_of_descriptions.append(desc)
        
    print(list_of_descriptions)

descriptions(tasks)

# 4. Print a list of tasks where time_taken is at least a given time

mins = int(input("Input minimum minutes: "))

def time_taken(list_of_tasks, mins):
    time = []

    for task in list_of_tasks:
        if task["time_taken"] >= mins:
            time.append(task)
    print(time)

time_taken(tasks, mins)




# 5. Print any task with a given description

desc_input = input("Enter description (from, Wash Dises, Clean Windows, Make Dinner, Feed Cat, Walk Dog: ")

def specific_task(list_of_tasks, description):
    for task in list_of_tasks:
        if task["description"] == description:
            print(task)

specific_task(tasks, desc_input)




# 6. Given a description update that task to mark it as complete.







# 7. Add a task to the list