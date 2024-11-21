import requests 
from sys import argv

id = argv[1]
url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
empurl= f'https://jsonplaceholder.typicode.com/users/{id}'

res1 = requests.get(url1)
data1 = res1.json()

res2 = requests.get(empurl)
data2 = res2.json()

EMPLOYEE_NAME = data2['name']
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = len(data1)
TASK_TITLE = []

for i in range(TOTAL_NUMBER_OF_TASKS):
    if(data1[i]['completed'])==True:
        NUMBER_OF_DONE_TASKS+=1
        TASK_TITLE.append(data1[i]['title'])

print(f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
for task in TASK_TITLE:
    print(f'\t {task}')