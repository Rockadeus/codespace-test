# Simple TODO List CLI Application

A command-line interface (CLI) application for managing your todo list, built with Python.

## Features

- Add new tasks
- List all tasks with their completion status

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

The application supports the following commands:

### Add a new task
```
python src/todo.py add "Your task description"
```

### List all tasks
```
python src/todo.py list
```

### Get help
```
python src/todo.py --help
```

## Data Storage

Tasks are stored in a `tasks.json` file in the root directory of the project.