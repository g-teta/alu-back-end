#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Get employee ID from command line argument
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # API endpoints
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get employee information
    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    employee_name = user.get("name")

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed") is True]

    # Display progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todos)}):")

    # Print completed task titles
    for task in done_tasks:
        print(f"\t {task.get('title')}")

