import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Please provide an ID as an argument.")
    sys.exit(1)

id = sys.argv[1]
url1 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
empurl = f'https://jsonplaceholder.typicode.com/users/{id}'

res1 = requests.get(url1)
if res1.status_code != 200:
    print(f"Error: Unable to fetch data from {url1}")
    sys.exit(1)
data1 = res1.json()

res2 = requests.get(empurl)
if res2.status_code != 200:
    print(f"Error: Unable to fetch data from {empurl}")
    sys.exit(1)
employeedata = res2.json()

USER_ID = employeedata['id']
USERNAME = employeedata['username']
TASK_COMPLETED_STATUS = ''
TOTAL_NUMBER_OF_TASKS = len(data1)
TASK_TITLE = ''

with open(f'{USER_ID}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['User ID', 'Username', 'Task Completed Status', 'Task Title'])
    for i in range(len(data1)):
        TASK_COMPLETED_STATUS = data1[i]['completed']
        TASK_TITLE = data1[i]['title']
        writer.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])