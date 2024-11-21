"""
This module makes 2 API requests and 
uses the information given to write it to a JSON file
"""

import json
import requests 
from sys import argv

def get_info(id):
    url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    empurl= f'https://jsonplaceholder.typicode.com/users/{id}'
    # Get todo tasks
    res1 = requests.get(url1)
    data1 = res1.json()
    # Get employee information
    res2 = requests.get(empurl)
    employeedata = res2.json()

    USER_ID = employeedata['id']
    USERNAME = employeedata['username']
    TOTAL_NUMBER_OF_TASKS = len(data1)
    tasks = []
    for task in data1:
        tasks.append({"task": task['title'], "completed": task['completed'], "username": USERNAME})
        
    dictionary = {USER_ID: tasks}
    with open(f'{id}.json', 'w') as file:
        json.dump(dictionary, file, indent=4)

if __name__ == "__main__":
    if len(argv) > 1:
        for arg in argv[1:]:
            get_info(int(arg))
    else:
        for i in range(1, 11):
            get_info(i)