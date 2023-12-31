from json import load, dump
from os import system
from time import sleep

# Clear interpreter variable
clear = lambda: system('cls')

# JSON file location
fileLocation = "simple-python-task-manager/json/task.json"

# Task Object
class Task:
    def __init__(self, taskIndex=0, taskTitle="", taskDecription="", taskStatus="Pending", taskCategories=[]):
        self._taskIndex = taskIndex
        self._taskTitle = taskTitle
        self._taskDescription = taskDecription
        self._taskStatus = taskStatus
        self._taskCategories = taskCategories

    def loadTask(self):
        # Initialize JSON file
        with open(fileLocation, "r") as task:

            # Loads JSON file content
            taskContent = load(task)

        return taskContent

    def createTask(self):
        # Task entry input
        title = self._taskTitle
        description = self._taskDescription
        status = self._taskStatus
        categories = self._taskCategories
        taskContent = self.loadTask()

        taskEntry = {"title": title, "description": description, "status": status, "categories": categories}

        # Initialize JSON file
        with open(fileLocation, "w") as task:

            # Append JSON file with new entry
            taskContent["tasks"].append(taskEntry)

            # Rewrite JSON file with updated entry
            dump(taskContent, task)

        return "Task added."

    def readTask(self, withStatistics=True):
        taskContent = self.loadTask()

        # Category list
        categories = []

        # Task Record Counter
        pendingTask = 0
        completedTask = 0
        totalTask = 0

        # Task entry header
        print(f"{'Index':<10}{'Title':^20}{'Description':^30}{'Status':^30}{'Categories':>20}")

        # Format Task Record
        for index, object in enumerate(taskContent["tasks"]):
            print(f"{index:<10}{object['title']:^20}{object['description']:^30}{object['status']:^30}{object['categories']}")

            # Increment Task Record Counters
            totalTask += 1
            if object['status'] == "Pending":
                pendingTask += 1
            elif object['status'] == "Completed":
                completedTask += 1

            # Get All Categories
            for category in object['categories']:
                categories.append(category.lower())

        # Completion Percentage Formula
        completionPercentage = (completedTask / totalTask) * 100

        if withStatistics == True:
            # Task Total and Completion Statistics
            print(f"{'-'*130}\nPending Task: {pendingTask}\nCompleted Task: {completedTask}\nTotal Tasks: {totalTask}\nCompletion Percentage: {completionPercentage:.2f} %\n{'-'*130}")

            # Task Category Statistics
            # Get unique categories
            uniqueCategories = list(set(categories))
            
            for uniqueCategory in uniqueCategories:
                categoryCounter = 0
                pendingCounter = 0
                completedCounter = 0
                for object in taskContent["tasks"]:
                    for categoryItem in object['categories']:
                        # Increase Category Counters
                        if uniqueCategory == categoryItem.lower():
                            categoryCounter += 1

                            if object['status'] == 'Pending':
                                pendingCounter += 1
                            elif object['status'] == 'Completed':
                                completedCounter += 1

                print(f"Total Task Record for category '{uniqueCategory}': {categoryCounter}\nPending: {pendingCounter}\nCompleted: {completedCounter}\n{'-'*130}")

    def updateTask(self):
        index = self._taskIndex
        taskContent = self.loadTask()

        try:
            # Remove Task based on index before updating
            selectedTask = taskContent["tasks"].pop(index)

            # Display selected record to update
            print("You have selected this Task to update:")
            print(f"{'Index':<10}{'Title':^20}{'Description':^30}{'Status':^30}{'Categories':>20}")
            print(f"{index:<10}{selectedTask['title']:^20}{selectedTask['description']:^30}{selectedTask['status']:^30}{selectedTask['categories']}")

            # Ask user what to update
            dataToUpdate = int(input("Select data to update: (1) Title, (2) Description, (3) Status, (4) Categories: "))

            # Update Title
            if dataToUpdate == 1:
                newTitle = input("Update Title: ")

                # Update selected Task Title
                selectedTask['title'] = newTitle

            # Update Description
            elif dataToUpdate == 2:
                newDescription = input("Update Description: ")

                # Update selected Task Description
                selectedTask['description'] = newDescription

            # Update Status
            elif dataToUpdate == 3:
                newStatus = int(input("Update Status: (1) Pending, (2) Completed: "))

                if newStatus == 1:
                    selectedTask['status'] = "Pending"
                elif newStatus == 2:
                    selectedTask['status'] = "Completed"
                else:
                    print("Invalid input.")

            # Update Categories
            elif dataToUpdate == 4:
                updateCategoryAction = int(input("Update Category Action: (1) Add, (2) Update, (3) Remove: "))

                if updateCategoryAction == 1:
                    newCategory = input("Enter Task Category: ")
                    selectedTask['categories'].append(newCategory)
                elif updateCategoryAction == 2:
                    # Select Category Header
                    print(f"{'Index':<10}{'Category':>10}")

                    # Display List of Category and Index
                    for index, category in enumerate(selectedTask['categories']):
                        print(f"{index:<10}{category:>10}")

                    # Select Category to Update
                    try:
                        selectCategoryIndex = int(input("Select Category Index to Update: "))

                        # Display Selected Category to Update
                        print(f"You selected category '{selectedTask['categories'][selectCategoryIndex]}'")

                        # New Category value
                        updateCategory = input("Update Category: ")
                        
                        # Update Category
                        selectedTask['categories'][selectCategoryIndex] = updateCategory

                    except IndexError:
                        return f"Task Category with index {selectCategoryIndex} does not exist."
                    
                elif updateCategoryAction == 3:
                    # Select Category Header
                    print(f"{'Index':<10}{'Category':>10}")

                    # Display List of Category and Index
                    for index, category in enumerate(selectedTask['categories']):
                        print(f"{index:<10}{category:>10}")

                    # Select Category to Update
                    try:
                        selectCategoryIndex = int(input("Select Category Index to Remove: "))

                        # Remove Category
                        selectedTask['categories'].pop(selectCategoryIndex)

                    except IndexError:
                        return f"Task Category with index {selectCategoryIndex} does not exist."

            else:
                print("Invalid input.")

            # Initialize JSON file
            with open(fileLocation, "w") as task:

                # Append JSON file with updated task
                taskContent["tasks"].append(selectedTask)

                # Rewrite JSON file with updated task
                dump(taskContent, task)
        
            return f"Task updated."
        
        except IndexError:
            return f"Task record with index {index} does not exist."

    def removeTask(self):
        try:
            index = self._taskIndex
            taskContent = self.loadTask()

            # Remove Task based on index
            taskContent["tasks"].pop(index)

            # Initialize JSON file
            with open(fileLocation, "w") as task:

                # Rewrite JSON file with updated entry
                dump(taskContent, task)

            return "Task removed."
        
        except IndexError:
            return f"Task record with index {index} does not exist."

# Welcome Message
print("Welcome to Simple Python Task Management System")

# Task Manager Logic
while True:
    try:
        userInput = int(input("Menu: (1) Add Task, (2) View Tasks, (3) Update Task, (4) Remove Task, (5) Exit Program: "))
        # Add Task
        if userInput == 1:
            categories = []
            enterCategory = 1

            # Task entry input
            title = input("Enter Task Title: ")
            description = input("Enter Task Description: ")

            # Multiple Category logic
            while enterCategory == 1:
                category = input("Enter Task Category: ")
                categories.append(category)
                enterCategory = int(input("Enter another category? (1) for Yes, (2) for No: "))

            # Initialize Task object
            task = Task(taskTitle=title, taskDecription=description, taskCategories=categories)
            
            # Call createTask method from Task object
            print(task.createTask())

        # View Tasks
        elif userInput == 2:
            # Initialize Task object
            tasks = Task()

            # Call readTask method from Task object
            tasks.readTask()

        # Update Tasks
        elif userInput == 3:
            # Initialize Task object for readTask method
            task = Task()

            # Update Task Confirmation Loop Condition
            updateTaskConfirmation = True

            # Update Task Loop Condition
            updateTask = True

            # Update Task Confirmation Loop
            while updateTaskConfirmation == True:
                try:
                    # User Confirmation to Remove Task
                    userConfirmation = int(input("To update tasks press (1) to go back the main menu press (2): "))

                    if userConfirmation == 1:
                        # Call readTask method without statistics
                        task.readTask(withStatistics=False)

                        # User Initial Update Input
                        taskIndexToUpdate = int(input("Select Task Index to update: "))

                        # Initialize Task Object
                        task = Task(taskIndex=taskIndexToUpdate)

                        # Call updateTask method from Task object
                        print(task.updateTask())

                        # Loop update task
                        while updateTask == True:
                            try:
                                # User Confirmation to Update Another Task
                                userConfirmation = int(input("Would you like to update another task press (1) for 'YES', press (2) to go back to the main menu: "))

                                if userConfirmation == 1:
                                    # Call readTask method without statistics
                                    task.readTask(withStatistics=False)
                                    
                                    # User Looped Update Input
                                    taskIndexToUpdate = int(input("Select Task Index to update: "))

                                    # Initialize Task Object
                                    task = Task(taskIndex=taskIndexToUpdate)

                                    # Call updateTask method from Task object
                                    print(task.updateTask())

                                elif userConfirmation == 2:
                                    # End While Loops for Confirmation and Task Update
                                    updateTaskConfirmation = False
                                    updateTask = False
                                else:
                                    print("Invalid input! The key selection is not part of the specified option.")
                            except ValueError:
                                print("The key selection is not an integer and is invalid.")

                    elif userConfirmation == 2:
                        updateTaskConfirmation = False

                    else:
                        print("Invalid input! The key selection is not part of the specified option.")

                except ValueError:
                    print("The key selection is not an integer and is invalid.")
                
                except ZeroDivisionError:
                    print("Task is empty.")

        # Remove Task
        elif userInput == 4:
            # Initialize Task object for readTask method
            task = Task()
            
            # Remove Task Confirmation Loop Condition
            removeTaskConfirmation = True

            # Remove Task Loop Condition
            removeTask = True

            # Remove Task Confirmation Loop
            while removeTaskConfirmation == True:
                try:
                    # User Confirmation to Remove Task
                    userConfirmation = int(input("To remove a task press (1) to go back the main menu press (2): "))

                    if userConfirmation == 1:
                        # Call readTask method without statistics
                        task.readTask(withStatistics=False)

                        # User Initial Input to Remove Task
                        taskIndexToRemove = int(input("Select Task Index to remove: "))

                        # Initialize Task object for removeTask method
                        task = Task(taskIndex=taskIndexToRemove)
                            
                        # Call removeTask method from Task object
                        print(task.removeTask())  

                        # Loop remove task
                        while removeTask == True:    
                            try:  
                                # User Confirmation to Remove Another Task
                                userConfirmation = int(input("Would you like to remove another task press (1) for 'YES', press (2) to go back to the main menu: "))

                                if userConfirmation == 1:
                                    # Call readTask method without statistics
                                    task.readTask(withStatistics=False)

                                    # User Looped Input to Remove Task
                                    taskIndexToRemove = int(input("Select Task Index to remove: "))

                                    # Initialize Task object for removeTask method
                                    task = Task(taskIndex=taskIndexToRemove)
                                        
                                    # Call removeTask method from Task object
                                    print(task.removeTask())  

                                elif userConfirmation == 2:
                                    # End While Loops for Confirmation and Task Removal
                                    removeTaskConfirmation = False
                                    removeTask = False
                                else:
                                    print("Invalid input! The key selection is not part of the specified option.")
                            except ValueError:
                                print("The key selection is not an integer and is invalid.")

                    elif userConfirmation == 2:
                        removeTaskConfirmation = False
                    
                    else:
                        print("Invalid input! The key selection is not part of the specified option.")
                
                except ValueError:
                    print("The key selection is not an integer and is invalid.")

                except ZeroDivisionError:
                    print("Task is empty.")

        # Exit Program
        elif userInput == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid input! The key selection is not part of the specified option.")

    except ValueError:
        print("The key selection is not an integer and is invalid.")

    except ZeroDivisionError:
        print("Task is empty.")

    except Exception as e:
        print(f"Error: {type(e).__name__}, Message: {e.args}")
    
    # Pause for n seconds after printing output
    sleep(5)

    # Clear screen for windows only
    clear()