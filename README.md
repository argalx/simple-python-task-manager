## Abount The Project
A simple task management system made in Python Programming Language that allows you to store task in a JSON file.

## JSON Schema for Task Manager Data
`{
    "tasks": [
        {
            "title": "",
            "description": "",
            "status": "",
            "categories": []
        }
}`

## Built With
- Python

## Getting Started
To run the program on your local machine follow these steps.

## Prerequisites
- Code Editor
    - VS Code, Notedpad, etc.
- Download and Install Python
    - Download latest version of Python for your machine from this link: https://www.python.org/downloads/
- Create JSON file with the following schema:
`{
    "tasks": [
        {
            "title": "",
            "description": "",
            "status": "",
            "categories": []
        }
}`
- Open task.py and update 'fileLocation' variable value to the path on where your JSON file is located

### How To Use
- Run the task.py
- Choose either of the following keys to navigate on the app:
1. Add Task
    - For Adding task supply the following data:
        - Title
        - Description
        - Category
2. View Tasks
3. Update Task
    - Choose the approriate keys to update the data for each task:
        1. Title (1)
        2. Description (2)
        3. Status (3)
        4. Category (4)
4. Remove Task
5. Exit Program    