#!/usr/bin/python3
"""A python script that parse data using the Restapi and save the
parsed data to json file
"""


import json
import requests


def all_employee_data():
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        todo_url = "https://jsonplaceholder.typicode.com/todos"

        users_data = requests.get(url).json()
        todo_data = requests.get(todo_url).json()

        results = {}

        for items in todo_data:
            emp_id = items['userId']
            data = {
                "username": next(user['username'] for user
                                 in users_data if
                                 user['id'] == emp_id),
                "task": items['title'],
                "completed": items['completed']
            }
            if emp_id not in results:
                results[emp_id] = []
            results[emp_id].append(data)
        sorted_result = dict(sorted(results.items()))

        with open("todo_all_employees.json", mode="w") as open_file:
            json.dump(sorted_result, open_file)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    all_employee_data()
