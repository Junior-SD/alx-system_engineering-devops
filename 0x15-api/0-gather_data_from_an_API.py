#!/usr/bin/python3
"""A python script that uses the REST API to return information on an employee
given the id
"""


import requests
from sys import argv


def employee_id():
    try:
        tmp = []
        emp_id = int(argv[1])
        url = "https://jsonplaceholder.typicode.com"
        emp_url = f'{url}/users/{emp_id}'
        todos_url = f'{url}/todos?userId={emp_id}'
        emp_data = requests.get(emp_url).json()
        todo_data = requests.get(todos_url).json()
        name = emp_data.get('name')
        count = sum(1 for comp in todo_data if comp['completed'] is True)

        print(f'Employee {name} is done with tasks({count}/{len(todo_data)}):')
        for tasks in todo_data:
            if tasks['completed']:
                lis = tasks.get('title')
                tmp.append(lis)
        for t in tmp:
            print(f'\t {t}')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    employee_id()
