#!/usr/bin/python3
"""A python script that parse data using the Rest Api and export parsed
data to json format
"""


import json
import requests
from sys import argv


def employee_id_json_converter():
    try:
        emp_id = int(argv[1])
        url = "https://jsonplaceholder.typicode.com"
        emp_url = f'{url}/users/{emp_id}'
        todo_url = f'{url}/todos?userId={emp_id}'
        data = []
        result = {}

        todo_data = requests.get(todo_url).json()
        emp_data = requests.get(emp_url).json()

        name = emp_data.get("username")
        for items in todo_data:
            data.append({
                "task": items['title'],
                "completed": items['completed'],
                "username": name,
            })
        result[f'{emp_id}'] = data
        with open(f'{emp_id}.json', mode="w") as open_file:
            json.dump(result, open_file)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    employee_id_json_converter()
